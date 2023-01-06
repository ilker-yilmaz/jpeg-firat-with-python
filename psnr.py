import os

import numpy as np
import cv2

my_img = cv2.imread('mini.jpg', cv2.IMREAD_GRAYSCALE)


def psnr(img, img_compressed):
    # Convert both images to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_compressed = cv2.cvtColor(img_compressed, cv2.COLOR_BGR2GRAY)

    mse = np.mean((img - img_compressed) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))


filepath = "c:\\users\\ilker\\Desktop\\jpeg-dct\\"

image_paths = [filepath + file for file in os.listdir(filepath)]


for path in image_paths:
    img = cv2.imread(path)
    print(psnr(my_img, img))
