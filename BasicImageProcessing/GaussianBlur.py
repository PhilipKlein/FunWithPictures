import numpy as np
from scipy import misc


def load_image( file_name ):
    image = imread(file_name)
    return image


def apply_gaussian_blur(img, sigma=1):
    # calculate the gaussian mask
    # apply 
    pass

def save_image(image, file_name):
    pass

if __name__ == "__main__":
    image = load_image("FarFarAway.jpg")
    image = apply_gaussian_blur(image)
    save_image(image, "FarFarAwayBlurred.jpg")
