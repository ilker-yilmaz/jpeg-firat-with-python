import cv2
import numpy as np
import os

# YCbCr renk uzayına dönüşüm matrisleri
YCbCr_transform = np.array([[0.299, 0.587, 0.114],
                           [-0.168736, -0.331264, 0.5],
                           [0.5, -0.418688, -0.081312]])

quantization_table = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
]

def RGB_to_YCbCr(image):
    height, width, _ = image.shape
    YCbCr_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            pixel = image[i, j]
            YCbCr_pixel = np.dot(YCbCr_transform, pixel)
            YCbCr_image[i, j] = YCbCr_pixel

    return YCbCr_image

def YCbCr_to_RGB(YCbCr_image):
    height, width, _ = YCbCr_image.shape
    RGB_image = np.zeros_like(YCbCr_image)

    for i in range(height):
        for j in range(width):
            pixel = YCbCr_image[i, j]
            RGB_pixel = np.dot(np.linalg.inv(YCbCr_transform), pixel)
            RGB_image[i, j] = RGB_pixel

    return RGB_image

def JPEG_compress(image_file, output_file):
    # Resmi yükle
    image = cv2.imread(image_file)
    height, width, _ = image.shape

    # Renk uzayını RGB'den YCbCr'ye dönüştür
    YCbCr_image = RGB_to_YCbCr(image)

    # Y kanalını 8x8 bloklara böl ve DCT uygula
    compressed_image = np.zeros_like(YCbCr_image)
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            block = YCbCr_image[i:i+8, j:j+8, 0]  # Y kanalı
            block_dct = cv2.dct(block.astype(np.float32))
            block_quantized = np.round(block_dct / quantization_table)
            compressed_image[i:i+8, j:j+8, 0] = block_quantized

    # Quantized katsayıları Huffman kodlaması ile sıkıştır
    # Bu adım, özel bir kütüphane kullanarak gerçekleştirilmelidir

    # Sıkıştırılmış görüntüyü YCbCr'den RGB'ye dönüştür
    compressed_image_rgb = YCbCr_to_RGB(compressed_image)

    # Sıkıştırılmış görüntüyü kaydet
    cv2.imwrite(output_file, compressed_image_rgb)

JPEG_compress("mini.jpg", "compressed.jpg")
