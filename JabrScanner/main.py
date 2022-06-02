from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    wrapped_img = np.zeros((output_width, output_height, 3))

    for i in range(len(img)):
        for j in range(len(img[0])):
            pixel = np.array([[i], [j], [1]])
            pixel = np.dot(transform_matrix, pixel)
            
            # 3D --> 2D
            pixel = np.array([pixel[0][0] / pixel[2][0], pixel[1][0] / pixel[2][0]])
            
            # assign the original img[i][j] values to the corresponding element in wrapped img
            # the if statement avoids index out of bounds
            if pixel[0] > 0 and pixel[0] < output_width and pixel[1] > 0 and pixel[1] < output_height:
                wrapped_img[int(pixel[0])][int(pixel[1])] = img[i][j]

    return wrapped_img    


def grayScaledFilter(img):
    grayScaleTransformMatrix = np.array([[0.299, 0.587, 0.114],
                                         [0.299, 0.587, 0.114],
                                         [0.299, 0.587, 0.114]])
    grayScaleImage = Filter(img, grayScaleTransformMatrix)

    return grayScaleImage


def crazyFilter(img):
    crazyTransformMatrix = np.array([[0,   0,   1], 
                                     [0,   0.5, 0], 
                                     [0.5, 0.5, 0]])
    crazyImage = Filter(img, crazyTransformMatrix)

    invCrazyTransformMatrix = np.linalg.inv(np.matrix(crazyTransformMatrix))
    invCrazyImage = Filter(crazyImage, invCrazyTransformMatrix)

    return crazyImage, invCrazyImage


def scaleImg(img, scale_width, scale_height):
    width = img.shape[0] * scale_width
    height = img.shape[1] * scale_height
    scaledImage = np.zeros((width, height, 3))

    for i in range(width):
        for j in range(height):
            scaledImage[i][j] = img[int(i / scale_width)][int(j / scale_height)]

    return scaledImage


def permuteFilter(img):
    permuteTransformMatrix = np.array([[0, 0, 1], 
                                       [0, 1, 0], 
                                       [1, 0, 0]])
    permuteImage = Filter(img, permuteTransformMatrix)

    return permuteImage


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[250, 16], [593, 179], [255, 984], [623, 906]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage, invertedCrazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")
    showImage(invertedCrazyImage, title="Inverted Crazy Filter")

    scaledImage = scaleImg(warpedImage, 3, 4)
    showImage(scaledImage, title="Scaled Image")

    permuteImage = permuteFilter(warpedImage)
    showImage(permuteImage, title="Permuted Image")
