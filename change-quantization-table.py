# from PIL import Image
# import numpy as np
#
# def change_quantization_table(image_path, quantization_table):
#     # Open the image
#     image = Image.open(image_path)
#
#     # Convert the image to YCbCr color space
#     image_ycbcr = image.convert('YCbCr')
#
#     # Split the image into Y, Cb, and Cr components
#     y, cb, cr = image_ycbcr.split()
#
#     # Convert the Y component to a NumPy array
#     y_array = np.array(y, dtype=np.float32)
#
#     # Modify the quantization table
#     for i in range(64):
#         y_array = np.round(y_array / quantization_table[i]) * quantization_table[i]
#
#     # Clip the values to the valid range
#     y_array = np.clip(y_array, 0, 255)
#
#     # Convert the modified Y component back to PIL Image format
#     modified_y = Image.fromarray(np.uint8(y_array), mode='L')
#
#     # Merge the modified Y component with the original Cb and Cr components
#     modified_image = Image.merge('YCbCr', (modified_y, cb, cr))
#
#     # Convert the image back to RGB format
#     modified_image_rgb = modified_image.convert('RGB')
#
#     # Save the modified image
#     modified_image_rgb.save('output.jpg')
#
# # Define your custom quantization table (example)
# custom_quantization_table = [16, 11, 10, 16, 24, 40, 51, 61,
#       12, 12, 14, 19, 26, 58, 60, 55,
#       14, 13, 16, 24, 40, 57, 69, 56,
#       14, 17, 22, 29, 51, 87, 80, 62,
#       18, 22, 37, 56, 68,109,103, 77,
#       24, 35, 55, 64, 81,104,113, 92,
#       49, 64, 78, 87,103,121,120,101,
#       72, 92, 95, 98,112,100,103, 99]
#
#
# # Call the function with your image path and the custom quantization table
# change_quantization_table('wp3293972.jpg', custom_quantization_table)


import jpegio as jio
import numpy as np

def change_quantization_table(image_path, quantization_table):
    # Load the JPEG image
    jpeg_struct = jio.read(image_path)

    # Modify the quantization table
    jpeg_struct.quant_tables[0] = quantization_table

    # Encode the modified image
    modified_jpeg_data = jio.encode(jpeg_struct)

    # Save the modified image
    with open('output.jpg', 'wb') as f:
        f.write(modified_jpeg_data)

# Define your custom quantization table (example)
custom_quantization_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
], dtype=np.uint8)

# Call the function with your image path and the custom quantization table
change_quantization_table('wp3293972.jpg', custom_quantization_table)
