from PIL import Image
import numpy as np

def jpeg_compress(image, quantization_table):
    # Görüntüyü YCbCr renk uzayına dönüştür
    ycbcr_image = image.convert("YCbCr")

    # Kanalları ayır
    y, cb, cr = ycbcr_image.split()

    # Y kanalını 8x8 bloklara böle
    y_blocks = block_split(y)

    # Her blok için DCT (Discrete Cosine Transform) uygula
    dct_blocks = dct_transform(y_blocks)

    # Kuantalama işlemi uygula
    quantized_blocks = quantize(dct_blocks, quantization_table)

    # Sıkıştırılmış verileri döndür
    return quantized_blocks

def block_split(channel):
    width, height = channel.size
    blocks = []
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            block = channel.crop((x, y, x + 8, y + 8))
            blocks.append(block)
    return blocks

def dct_transform(blocks):
    transformed_blocks = []
    for block in blocks:
        data = np.asarray(block, dtype=np.float32) - 128.0
        dct_data = np.zeros_like(data)
        for v in range(8):
            for u in range(8):
                alpha_u = 1.0 / np.sqrt(8.0) if u == 0 else np.sqrt(2.0 / 8.0)
                alpha_v = 1.0 / np.sqrt(8.0) if v == 0 else np.sqrt(2.0 / 8.0)
                sum_val = 0.0
                for y in range(8):
                    for x in range(8):
                        sum_val += data[y, x] * np.cos(((2 * x + 1) * u * np.pi) / 16) * np.cos(
                            ((2 * y + 1) * v * np.pi) / 16
                        )
                dct_data[v, u] = alpha_u * alpha_v * sum_val
        transformed_blocks.append(dct_data)
    return transformed_blocks

def quantize(blocks, quantization_table):
    quantized_blocks = []
    for block in blocks:
        quantized_block = np.round(block / quantization_table)
        quantized_blocks.append(quantized_block.astype(np.int16))
    return quantized_blocks

# Kuantalama tablolarının olduğu .txt dosyasının yolu
quantization_tables_path = "nicelemetablolari_son.txt"

# Görüntülerin olduğu dizin
image_directory = "C:/Users/ilker/Desktop/pnomoni/"

# Kuantalama tablolarını yükle
with open(quantization_tables_path, "r") as file:
    quantization_tables = file.read().split("\n\n")

# Her bir görüntüyü sıkıştır ve kaydet
for i in range(1, 101):
    image_path = f"{image_directory}goruntu_{i}.jpg"
    image = Image.open(image_path)

    # Görüntüye uygun kuantalama tablosunu seç
    if i % 2 == 0:
        quantization_table = np.loadtxt(quantization_tables[0], dtype=np.float32)
    else:
        quantization_table = np.loadtxt(quantization_tables[1], dtype=np.float32)

    compressed_image = jpeg_compress(image, quantization_table)

    # Sıkıştırılmış görüntüyü kaydet
    save_path = f"{image_directory}goruntu_{i}_compressed.jpg"
    compressed_image = Image.fromarray(compressed_image)
    compressed_image.save(save_path, "JPEG")
