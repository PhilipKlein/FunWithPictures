import numpy as np
from scipy import misc

def load_image(image_file):
    row_image = misc.imread(image_file)
    return row_image


def save_image(new_image, file_name):
    misc.toimage(new_image).save(file_name)


def change_brightness(image_to_change, bias):
    brighter_image = np.empty_like(image_to_change)
    for i in range(0, len(image_to_change)):
        for j in range(0, len(image_to_change[i])):
            #for color in range(0, len(image_to_change[i][j])): #first check whether its rgb image or not.
            brightened_val = image_to_change[i][j] + bias
            brighter_image[i][j] = np.uint8(brightened_val)
    return brighter_image

def conv_filter():
    s = (3, 3)
    mask = np.zeros(s)
    mask[0] = [0, 1, 0]
    mask[1]  = [1, 4, 1]
    mask[2] = [0, 1, 0]
    return mask

def calc_gaussian_kernel(variance):
    return

def control_pixel(i, j, size):
    if i == 0 or j == 0:
        return False
    elif i == size or j == size:
        return False
    return True

def calc_mult(image, filter, i, j):
    start_i = i - 1
    sum = 0
    filter_sum = 0
    for index_i in range(0, len(filter)):
        start_j = j -1
        for index_j in range(0, len(filter)):
            sum += (image[start_i][start_j]*filter[index_i][index_j])
            start_j += 1
            filter_sum += filter[index_i][index_j]
        start_i += 1
    if filter_sum == 0:
        filter_sum += 1
    return np.uint8(sum / filter_sum)

def convolution(image, filter):
    size = len(filter)
    for i in range(0, len(image)):
        for j in range(0, len(image)):
            if control_pixel(i, j, len(image) - 1) is True:
                image[i][j] = calc_mult(image, filter, i, j)
    return image

if __name__ == "__main__":
    image = load_image("new_lena.png")
    conv_mask = conv_filter()
    image = convolution(image, conv_mask)
    #image = change_brightness(image, 20)
    save_image(image, "new_lena.png")




