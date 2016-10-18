import cv2 as cv
import numpy as np


def point1():
    l1_image = cv.imread("L1.jpg", 0)
    height, width = l1_image.shape[:2]

    for i in range(0, height):
        for j in range(0, width):
            if l1_image[i][j] > 127:
                l1_image[i][j] = 255
            else:
                l1_image[i][j] = 0

    cv.namedWindow("Point 1", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 1", l1_image)
    cv.waitKey(0)


def point2():
    l1_image = cv.imread("L1.jpg", 0)
    logo_image = cv.imread("logo.jpg", 0)
    resultSizeSAmple = cv.imread("L1.jpg", 0)
    resizedLogoImage = resize_image(resultSizeSAmple, logo_image)
    l1_height, l1_width = l1_image.shape[:2]
    for i in range(0, l1_height):
        for j in range(0, l1_width):
            new_value = (l1_image[i][j] * 0.8) + (resizedLogoImage[i][j] * 0.2)
            if new_value > 255:
                new_value = 255
            l1_image[i][j] = new_value

    cv.namedWindow("Point 2", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 2", l1_image)
    cv.waitKey(0)


def resize_image(resultSizeSample, image):
    # return cv.resize(image, (newWidth, newHeight))
    newHeight, newWidth = resultSizeSample.shape[:2]
    originalHeight, originalWidth = image.shape[:2]
    xScallingFactor = newWidth * 1.0 / originalWidth
    yScallingFactor = newHeight * 1.0 / originalHeight
    scallingMatrix = np.matrix([[xScallingFactor, 0.0], [0.0, yScallingFactor]])
    scallingMatrixInverse = np.linalg.inv(scallingMatrix)
    for x in range(0, newWidth):
        for y in range(0, newHeight):
            sourcePixel = scallingMatrixInverse * np.matrix([[x], [y]])
            # res[y, x] = image[int(sourcePixel[1, 0]), int(sourcePixel[0, 0])]
            if sourcePixel[0, 0] == int(sourcePixel[0, 0]) and sourcePixel[1, 0] == int(sourcePixel[1, 0]):
                resultSizeSample[y][x] = image[int(sourcePixel[1, 0]), int(sourcePixel[0, 0])]
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
                resultSizeSample[y][x] = i
        print x, " out of ", newWidth - 1
    return resultSizeSample


# TODO - MAKE SURE IT IS JUST ADDITION
def point3():
    l2_image = cv.imread("L2.jpg", 0)
    l2_height, l2_width = l2_image.shape[:2]

    for i in range(0, l2_height):
        for j in range(0, l2_width):
            l2_image[i][j] += 50
            if l2_image[i][j] > 255:
                l2_image[i][j] = 255

    cv.namedWindow("Point 3", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 3", l2_image)
    cv.waitKey(0)


def point4():
    l3_image = cv.imread("L3.jpg", 0)
    l3_height, l3_width = l3_image.shape[:2]

    cv.namedWindow("Point 3", cv.WINDOW_NORMAL)
    cv.imshow("Point 3", l3_image)
    cv.waitKey(0)


point2()
