import numpy as np
from scipy import ndimage

def rgba2rgb(rgba, background=(1,1,1)):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'RGBA image has 4 channels.'

    rgb = np.zeros( (row, col, 3), dtype='float32' )
    r, g, b, a = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]
    #print(r)
    #print(a)

    #a = np.asarray( a, dtype='float32' ) / 1

    R, G, B = background

    rgb[:,:,0] = r * a + (1.0 - a) * R
    rgb[:,:,1] = g * a + (1.0 - a) * G
    rgb[:,:,2] = b * a + (1.0 - a) * B

    return np.asarray( rgb, dtype='float32' )

def gray2binary(gray):
    threshold = 0.5
    for x in range(0, len(gray[1])):
        for y in range(0, len(gray)):
            if (gray[y][x]>threshold):
                gray[y][x] = 0
            else:
                gray[y][x] = 1
    return gray

def erode(image, horizontal=1, elem_size=30):
    x_size = image.shape[1]
    y_size = image.shape[0]
    new_image = np.zeros((y_size,x_size))
    element = []
    if horizontal:
        index_0 = int((elem_size/2) - 1)
        index_end = int(x_size-(elem_size/2)-1)
        for y in range(0, y_size):
            #Build the morphological element
            element.clear()
            for i in range(0,elem_size):
                element.append(image[y][i])
            for x in range(index_0, index_end+1):
                new_image[y][x] = min(element)
                element.pop(0)
                element.append(image[y][int(x+(elem_size/2))])
    return new_image

def dilation(image, horizontal=1, elem_size=30):
    x_size = image.shape[1]
    y_size = image.shape[0]
    new_image = np.zeros((y_size,x_size))
    element = []
    if horizontal:
        index_0 = int((elem_size/2) - 1)
        index_end = int(x_size-(elem_size/2)-1)
        for y in range(0, y_size):
            #Build the morphological element
            element.clear()
            for i in range(0,elem_size):
                element.append(image[y][i])
            for x in range(index_0, index_end+1):
                new_image[y][x] = max(element)
                element.pop(0)
                element.append(image[y][int(x+(elem_size/2))])
    return new_image

def edge_det(image):
    kernel = np.array([[ -1, -1, -1, -1, -1],
                        [-1,  1,  2,  1, -1],
                        [-1,  2,  4,  2, -1],
                        [-1,  1,  2,  1, -1],
                        [-1, -1, -1, -1, -1]])
    highpass = ndimage.convolve(image, kernel)
    return highpass