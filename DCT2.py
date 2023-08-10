import cv2
import numpy as np
import os
import sys
import json


# Quantization tablolarını JSON dosyasından okuma
loaded_quantalama = []
with open("quantization-table.json", "r") as file:
    loaded_quantalama = json.load(file)

quantalama = loaded_quantalama
# 07.08.2023
def JPEG_DCT(imgfile, file, type):
    img = cv2.imread(imgfile)  # Renkli olarak okuma

    iHeight, iWidth, _ = img.shape  # Renkli görüntü olduğu için üçüncü boyut da kullanılır

    if (iWidth % 8) != 0: # Görüntü 8'e tam bölünmüyorsa
        filler = img[:, iWidth-1:] # Son sütunu al
        for i in range(8 - (iWidth % 8)): # 8'e tam bölünene kadar son sütunu ekle
            img = np.append(img, filler, 1) # Son sütunu görüntüye ekle

    if (iHeight % 8) != 0: # Görüntü 8'e tam bölünmüyorsa
        filler = img[iHeight-1:, :] # Son satırı al
        for i in range(8 - (iHeight % 8)): # 8'e tam bölünene kadar son satırı ekle
            img = np.append(img, filler, 0) # Son satırı görüntüye ekle

    iHeight, iWidth, _ = img.shape # Görüntü yeniden boyutlandırıldığı için boyutlar değişir

    img2 = np.empty(shape=(iHeight, iWidth, 3))  # Üçüncü boyut da eklenir

    for startY in range(0, iHeight, 8): # 8x8 bloklar halinde görüntüyü dolaş
        for startX in range(0, iWidth, 8): # 8x8 bloklar halinde görüntüyü dolaş
            for channel in range(3): # Renk kanalları için
                block = img[startY:startY+8, startX:startX+8, channel] # 8x8 blok al

                # apply DCT for each color channel
                blockf = np.float32(block) # convert integers to floats
                dst = cv2.dct(blockf) # apply discrete cosine transform

                if (startY == 0 and startX == 0): # ilk blok için
                    dctval = dst # ilk bloğun DCT katsayılarını sakla

                # quantization of the DCT coefficients
                blockq = np.around(np.divide(dst, std_luminance_quant_tbl)) # quantize the DCT coefficients
                blockq = np.multiply(blockq, std_luminance_quant_tbl) # dequantize the DCT coefficients

                # store the result
                for y in range(8): # 8x8 blok için
                    for x in range(8): # 8x8 blok için
                        img2[startY+y, startX+x, channel] = blockq[y, x] # bloğu görüntüye ekle

    block1 = img[0:8, 0:8, :] # ilk bloğu al
    block1 = img2[0:8, 0:8, :] # ilk bloğu al

    for startY in range(0, iHeight, 8): # 8x8 bloklar halinde görüntüyü dolaş
        for startX in range(0, iWidth, 8): # 8x8 bloklar halinde görüntüyü dolaş
            for channel in range(3): # Renk kanalları için
                block = img2[startY:startY+8, startX:startX+8, channel] # 8x8 blok al

                blockf = np.float32(block) # convert integers to floats
                dst = cv2.idct(blockf) # apply inverse discrete cosine transform
                np.place(dst, dst > 255.0, 255.0) # clip values above 255
                np.place(dst, dst < 0.0, 0.0) # clip values below 0
                block = np.uint8(np.around(dst)) # convert floats to integers

                # store the results
                for y in range(8): # 8x8 blok için
                    for x in range(8): # 8x8 blok için
                        img[startY+y, startX+x, channel] = block[y, x] # bloğu görüntüye ekle

    block1 = img[0:8, 0:8, :] # ilk bloğu al
    # print "Reverse (1st block):\n", block1

    file1 = "c:\\users\\ilker\\Desktop\\jpeg-dct-3\\" + file + ".jpg" # dosya adı
    cv2.imwrite(file1, img) # görüntüyü kaydet

    b = os.path.getsize(file1)

type = 0 # 0: 8x8, 1: 16x16, 2: 32x32

for i in range(0, len(quantalama)): # 0'dan 63'e kadar
    file = 'c' + str(i) # dosya adı

    matrix_firat = quantalama[i] # quantalama matrisi
    if (len(sys.argv) > 1): # komut satırı parametreleri
        file = str(sys.argv[1]) # dosya adı

    if (len(sys.argv) > 2): # komut satırı parametreleri
        type = int(sys.argv[2]) # dosya adı

    if (len(sys.argv) > 3): # komut satırı parametreleri
        matrix_firat = str(sys.argv[3]) # dosya adı

    std_luminance_quant_tbl = eval(str(matrix_firat)) # quantalama matrisi

    JPEG_DCT("1.jpg", file, type) # JPEG DCT fonksiyonu
    i += 1 # i'yi bir arttır
