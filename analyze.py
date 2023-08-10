import os
import numpy as np
from PIL import Image
import math

def calculate_metrics(original_image_path, compressed_images_folder):
    # Load the original image
    original_img = Image.open(original_image_path)
    original_array = np.array(original_img)

    # Initialize a list to store results
    results = []

    # Iterate through compressed images
    for filename in os.listdir(compressed_images_folder):
        if filename.endswith(".jpg"):
            compressed_image_path = os.path.join(compressed_images_folder, filename)
            compressed_img = Image.open(compressed_image_path)
            compressed_array = np.array(compressed_img)

            # Calculate BPP
            compressed_size_bits = os.path.getsize(compressed_image_path) * 8
            bpp = compressed_size_bits / (original_array.shape[0] * original_array.shape[1])

            # Calculate CR
            original_size_bits = os.path.getsize(original_image_path) * 8
            cr = original_size_bits / compressed_size_bits

            # Calculate PSNR
            mse = np.mean((original_array - compressed_array) ** 2)
            psnr = 10 * math.log10(255 ** 2 / mse)

            results.append({
                "Filename": filename,
                "BPP": bpp,
                "CR": cr,
                "PSNR": psnr
            })

    # Sort results by PSNR in descending order
    sorted_results = sorted(results, key=lambda x: x["PSNR"], reverse=True)

    # Print the top 10 results
    print("Top 10 Results:")
    for i, result in enumerate(sorted_results[:10], 1):
        print(f"{i}. Filename: {result['Filename']}, BPP: {result['BPP']:.2f}, CR: {result['CR']:.2f}, PSNR: {result['PSNR']:.2f}")

# Provide paths to the original image and compressed images folder
original_image_path = "1.jpg"
compressed_images_folder = "C:/Users/ilker/Desktop/jpeg-dct-3"

calculate_metrics(original_image_path, compressed_images_folder)
