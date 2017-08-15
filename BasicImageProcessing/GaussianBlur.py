import numpy as np
from scipy import misc
from math import floor, pow, fabs
from math import e as EULER
from math import pi as PI


def load_image( file_name ):
    image = misc.imread(file_name)
    return image


def _generate_mask(sigma, kernel_size):
    """ Generate the mask for the gaussian blur formula taken from 
    https://en.wikipedia.org/wiki/Gaussian_blur"""
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
    return gf


def apply_gaussian_blur(img, sigma=1, kernel_size=5):
    """ Applies gaussian blur
        sigma: determines influence of outside pixel
        kernel_size: how many pixels outside get calculated, 
                     CARE: High values decrease performance repidely,
        TODO: parallelize for loop
    """
    if kernel_size % 2 != 1: # if kernel_size even return error
        print("Kernel size has to be odd")
        return
    center = floor(kernel_size/2)
    gf = _generate_mask(sigma, kernel_size)

    blurred_image = np.copy(image)
    print(image.shape)
    x_len = image.shape[0]
    y_len = image.shape[1]
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            for color in range(len(img[i][j])):
                temp = 0
                for x_dis in range(-center, center + 1):
                    for y_dis in range(-center, center + 1):
                        # Handle the edge case by mirroring
                        x_pix = i+x_dis
                        if (x_pix < 0):
                            x_pix = abs(x_pix)
                        elif (x_pix >= x_len):
                            x_pix -= x_pix-x_len
                            x_pix -= 1
                        y_pix = j + y_dis
                        if (y_pix < 0):
                            y_pix = abs(y_pix)
                        elif (y_pix >= y_len):
                            y_pix -= y_pix-y_len
                            y_pix -= 1
                        temp += image[x_pix][y_pix][color]*gf[x_dis+center][y_dis + center]
                temp = np.ceil(temp) # do rounding correctly
                blurred_image[i][j][color] = np.uint8(temp)

    
    return blurred_image

def save_image(image, file_name):
    misc.toimage(image).save(file_name)

if __name__ == "__main__":
    image = load_image("FarFarAway.jpg")
    image = apply_gaussian_blur(image)
    save_image(image, "FarFarAwayBlurred.jpg")
