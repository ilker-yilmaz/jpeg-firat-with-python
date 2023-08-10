import cv2
import numpy as np
import os
import sys
import json

# Quantization tablolarını JSON dosyasından okuma
loaded_quantization = []
with open("quantization-table.json", "r") as file:
    loaded_quantization = json.load(file)

# Kuantalama matrisini seçin
quantization_matrix = loaded_quantization[0]  # Örneğin, ilk matrisi kullanıyoruz

def JPEG_DCT(imgfile, outputfile):
    img = cv2.imread(imgfile)  # Renkli olarak okuma

    # Görüntüyü 8'e tam bölünür hale getirme
    new_height = (img.shape[0] // 8) * 8
    new_width = (img.shape[1] // 8) * 8
    img = img[:new_height, :new_width, :]

    img2 = np.empty_like(img)  # Aynı boyutta boş bir görüntü oluştur

    for startY in range(0, new_height, 8):  # 8x8 bloklar halinde görüntüyü dolaş
        for startX in range(0, new_width, 8):  # 8x8 bloklar halinde görüntüyü dolaş
            for channel in range(3):  # Renk kanalları için
                block = img[startY:startY+8, startX:startX+8, channel]  # 8x8 blok al

                # DCT işlemi
                dst = cv2.dct(np.float32(block))

                if (startY == 0 and startX == 0):
                    dctval = dst

                # Kuantalama
                blockq = np.around(np.divide(dst, quantization_matrix))
                blockq = np.multiply(blockq, quantization_matrix)

                # Ters DCT işlemi
                inv_dst = cv2.idct(blockq)
                np.place(inv_dst, inv_dst > 255.0, 255.0)
                np.place(inv_dst, inv_dst < 0.0, 0.0)
                block_restored = np.uint8(np.around(inv_dst))

                # Sonuçları sakla
                img2[startY:startY+8, startX:startX+8, channel] = block_restored

    cv2.imwrite(outputfile, img2)

input_image = "1.jpg"  # Orjinal görüntü
output_folder = "C:/Users/ilker/Desktop/compressed_images"  # Sıkıştırılmış görüntülerin kaydedileceği klasör

os.makedirs(output_folder, exist_ok=True)  # Çıktı klasörünü oluştur

# Tüm quantalama matrisleri için işlemi yap
for i, quant_matrix in enumerate(loaded_quantization):
    output_file = os.path.join(output_folder, f"compressed_{i}.jpg")
    JPEG_DCT(input_image, output_file)
    print(f"Compressed image saved as: {output_file}")
