import numpy as np
from scipy import misc
from math import floor, pow, fabs
from math import e as EULER
from math import pi as PI


def load_image( file_name ):
    image = misc.imread(file_name)
    return image


def apply_gaussian_blur(img, sigma=1, kernel_size=5):
    if kernel_size % 2 != 1: # if kernel_size even return error
        print("Kernel size has to be odd")
        return
    # generate and normalize matrix
    center = floor(kernel_size/2)
    gf = np.empty((kernel_size, kernel_size), dtype=float)
    for i in range(0, kernel_size):
        for j in range(0, kernel_size):
            x = fabs(center - i)
            y = fabs(center - j)
            gf[i][j] = (1/(2*PI*sigma*sigma))*pow(EULER, -((x*x + y*y) / (2*sigma)))
    sum_of_all_values = sum(sum(gf))
    for i in range(len(gf)):
        for j in range(len(gf[i])):
            gf[i][j] = gf[i][j]/sum_of_all_values

    # apply the filter on image
    blurred_image = np.copy(image)
    for i in range(center, len(img) -center ):
        for j in range(center, len(img[i]) - center): # iterate over rows
            for color in range(len(img[i][j])): #iterate over columns
                # Ignoring edges for now
                temp = 0
                for x_dis in range(-center, center):
                    for y_dis in range(-center, center):
                        temp += image[i+x_dis][j+y_dis][color]*gf[x_dis+center][y_dis + center]
                blurred_image[i][j][color] = np.uint8(temp)

    
    return blurred_image

def save_image(image, file_name):
    misc.toimage(image).save(file_name)

if __name__ == "__main__":
    image = load_image("FarFarAway.jpg")
    image = apply_gaussian_blur(image)
    save_image(image, "FarFarAwayBlurred.jpg")
