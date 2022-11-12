import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

file1 = '1111'

matrix = "[ [0, 21, 21, 22, 22, 22, 22, 22], [21, 21, 21, 21, 21, 21, 21, 21], " \
         "[21, 21, 21, 21, 21, 21, 21, 21], [21,21,21,21,21,20,20,20], " \
         "[22, 22, 22, 22, 21, 21, 21, 21], [24, 24, 24, 23, 23, 22, 22, 22], " \
         "[26, 26, 25, 25, 24, 24, 24, 23], [27, 27, 27, 26, 25, 25, 25, 24]]"

if (len(sys.argv) > 1):
    matrix = str(sys.argv[1])

if (len(sys.argv) > 2):
    file = str(sys.argv[2])

block = eval(matrix)

print("Input:\n", block)

blockf = np.float32(block)  # float conversion

dst = cv2.dct(blockf)

print("\nDCT:\n", np.int32(dst))

block = cv2.idct(dst)

print
"\nInverse DCT:\n", np.int32(block)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x, y = np.meshgrid(x, y)

plt.pcolormesh(x, y, block, vmin=0, vmax=255)
plt.colorbar()

plt.show()