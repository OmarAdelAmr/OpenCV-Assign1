import cv2 as cv


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
    l1_height, l1_width = l1_image.shape[:2]
    logo_image = resize_image(cv.imread("logo.jpg", 0), l1_width, l1_height)

    for i in range(0, l1_height):
        for j in range(0, l1_width):
            new_value = (l1_image[i][j] * 0.8) + (logo_image[i][j] * 0.2)
            if new_value > 255:
                new_value = 255
            l1_image[i][j] = new_value

    cv.namedWindow("Point 2", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 2", l1_image)
    cv.waitKey(0)


# TODO - ASk IF i SHOULD HARD-CODE IT
def resize_image(image, width, height):
    return cv.resize(image, (width, height))


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
    l3_image = cv.imread("L2.jpg", 0)
    l3_height, l3_width = l3_image.shape[:2]

    cv.namedWindow("Point 3", cv.WINDOW_AUTOSIZE)
    cv.imshow("Point 3", l3_image)
    cv.waitKey(0)


point4()
