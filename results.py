import os

import cv2

filepath = "c:\\users\\ilker\\Desktop\\jpeg-dct\\"

image_paths = [filepath + file for file in os.listdir(filepath)]


for path in image_paths:
    img = cv2.imread(path)
    if img is None:
        print(f"{path}: Dosya okunamadı")
    else:
        size = img.nbytes
        print(f"{path}: {size} bytes")




