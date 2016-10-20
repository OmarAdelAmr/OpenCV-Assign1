import cv2 as cv
import numpy as np


def point1():
    l1_image = cv.imread("L1.jpg", 0)
    height, width = l1_image.shape[:2]
    result = np.zeros((height, width), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            if l1_image[i][j] > 127:
                result[i][j] = 255
            else:
                result[i][j] = 0

    cv.namedWindow("Point 1", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 1", result)
    cv.waitKey(0)


def point2():
    l1_image = cv.imread("L1.jpg", 0)
    logo_image = cv.imread("logo.jpg", 0)
    l1_height, l1_width = l1_image.shape[:2]
    resizedLogoImage = resize_image(logo_image, l1_height, l1_width)
    result = np.zeros((l1_height, l1_width), np.uint8)
    for i in range(0, l1_height):
        for j in range(0, l1_width):
            new_value = (l1_image[i][j] * 0.8) + (resizedLogoImage[i][j] * 0.2)
            if new_value > 255:
                new_value = 255
            result[i][j] = new_value

    cv.namedWindow("Point 2", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 2", result)
    cv.waitKey(0)


def resize_image(image, height, width):
    # return cv.resize(image, (669, 325))
    result = np.zeros((height, width), np.uint8)
    originalHeight, originalWidth = image.shape[:2]
    xScallingFactor = width * 1.0 / originalWidth
    yScallingFactor = height * 1.0 / originalHeight
    scallingMatrix = np.matrix([[xScallingFactor, 0.0], [0.0, yScallingFactor]])
    scallingMatrixInverse = np.linalg.inv(scallingMatrix)
    for x in range(0, width):
        for y in range(0, height):
            sourcePixel = scallingMatrixInverse * np.matrix([[x], [y]])
            # res[y, x] = image[int(sourcePixel[1, 0]), int(sourcePixel[0, 0])]
            if sourcePixel[0, 0] == int(sourcePixel[0, 0]) and sourcePixel[1, 0] == int(sourcePixel[1, 0]):
                result[y][x] = image[int(sourcePixel[1, 0]), int(sourcePixel[0, 0])]
            else:
                xSourceFloor = int(sourcePixel[0])
                xSourceCeiling = int(sourcePixel[0] + 1)
                ySourceFloor = int(sourcePixel[1])
                ySourceCeiling = int(sourcePixel[1] + 1)
                i1Factor = sourcePixel[0] - int(sourcePixel[0])
                i2Factor = sourcePixel[1] - int(sourcePixel[1])
                i2 = 255
                i1 = image[ySourceFloor][xSourceFloor] * (1.0 - i1Factor)
                if ySourceCeiling < originalHeight:
                    i1 += image[ySourceCeiling][xSourceFloor] * i1Factor
                if xSourceCeiling < originalWidth:
                    i2 = image[ySourceFloor][xSourceCeiling] * (1.0 - i1Factor)
                if ySourceCeiling < originalHeight and xSourceCeiling < originalWidth:
                    i2 += image[ySourceCeiling][xSourceCeiling] * i1Factor
                i = (i1 * (1 - i2Factor) + i2 * i2Factor)
                if i > 255:
                    i = 255
                result[y][x] = i
        print "column", x, " out of ", width - 1
    return result


# TODO - MAKE SURE IT IS JUST ADDITION
def point3():
    l2_image = cv.imread("L2.jpg", 0)
    l2_height, l2_width = l2_image.shape[:2]
    result = np.zeros((l2_height, l2_width), np.uint8)
    for i in range(0, l2_height):
        for j in range(0, l2_width):
            newVal = l2_image[i][j] + 50
            if newVal > 255:
                result[i][j] = 255
            else:
                result[i][j] = newVal

    cv.namedWindow("Point 3", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 3", result)
    cv.waitKey(0)


def point4():
    l3_image = cv.imread("L3.jpg", 0)
    l3_height, l3_width = l3_image.shape[:2]
    result = np.zeros((l3_height, l3_width), np.uint8)
    oldVals = np.matrix([[65, 475, 1], [1000, 135, 1], [5, 5, 1]])
    newX = np.matrix([[5], [1008], [5]])
    newY = np.matrix([[480], [5], [5]])
    affineMat = calculateAffineMAtrix(oldVals, newX, newY)
    for x in range(0, l3_width):
        for y in range(0, l3_height):
            dest = affineMat * np.matrix([[x], [y], [1]])
            newX = dest[0][0]
            newY = dest[1][0]
            if newX < l3_width and newX >= 0 and newY < l3_height and newY >= 0:
                result[int(newY)][int(newX)] = l3_image[y, x]

        print "Column", x, "out of ", l3_width

    cv.namedWindow("Point 4", cv.WINDOW_NORMAL)
    cv.imshow("Point 4", result)
    cv.waitKey(0)


def calculateAffineMAtrix(oldVals, newX, newY):
    oldValsInv = np.linalg.inv(oldVals)
    ones = np.matrix([[1], [1], [1]])
    a1 = oldValsInv * newX
    a2 = oldValsInv * newY
    a3 = oldValsInv * ones
    result = np.zeros(shape=(3, 3))
    result[0] = a1.transpose()
    result[1] = a2.transpose()
    result[2] = a3.transpose()
    return result


def point5():
    l4_image = cv.imread("L4.jpg", 0)
    l4_height, l4_width = l4_image.shape[:2]
    result = np.zeros((l4_height, l4_width), np.uint8)
    sourcePoints = np.array([[50.0, 55], [190, 20], [190, 150], [50, 185]])
    endPoints = np.array([[0.0, 0], [145, 0], [145, 130], [0, 130]])
    h, status = cv.findHomography(sourcePoints, endPoints)
    result = cv.warpPerspective(l4_image, h, (l4_image.shape[1], l4_image.shape[0]))
    # for x in range(0, l4_width):
    #     for y in range(0, l4_height):
    #         dest = h * np.matrix([[x], [y], [1]])
    #         newX = dest[0][0]
    #         newY = dest[1][0]
    #         if newX < l4_width and newX >= 0 and newY < l4_height and newY >= 0:
    #             result[int(newY)][int(newX)] = l4_image[y, x]
    #     print x
    cv.namedWindow("Point 5", cv.WINDOW_NORMAL)
    cv.imshow("Point 5", result)
    cv.waitKey(0)


def main():
    userInput = raw_input("Enter 1, 2, 3, 4 or 5 for points from 1 to 5 respectively: ")
    try:
        val = int(userInput)
    except ValueError:
        print("That's not an int!")
        main()
    if val == 1:
        point1()
    elif val == 2:
        point2()
    elif val == 3:
        point3()
    elif val == 4:
        point4()
    elif val == 5:
        point5()


main()
