import numpy as np

# quantalama.txt dosyasını okuyalım ve her 8*8 lik matrisi araya virgüller koyarak bir listeye atalım
with open('quantalama.txt') as f:
    quantalama = f.read().split(']]')
    print(quantalama[0])

    # her quantalama değerinin sonuna ]] ekle
    for i in range(len(quantalama)):
        quantalama[i] = quantalama[i] + ']]'
    print(type(quantalama))
    print(len(quantalama))
    print(quantalama[801])
#
list = [[[26, 29, 27, 28, 30, 34, 29, 31],
         [36, 39, 37, 35, 42, 39, 42, 40],
         [43, 44, 48, 49, 47, 48, 48, 55],
         [48, 49, 55, 48, 54, 55, 59, 60],
         [58, 61, 64, 63, 63, 64, 64, 66],
         [69, 64, 69, 71, 75, 71, 75, 78],
         [72, 73, 78, 78, 80, 81, 81, 82],
         [78, 84, 89, 87, 87, 89, 90, 94]],
        ]

# list[0] ile list[1] arasındaski farklılıkları bulalım
#print(np.array(list[0]) - np.array(list[4]))

quantalamalarımız = []
# create the quantization tables for dct. use the range function. 0-255 arası değerler için 8*8 lik matrisler oluştur

print(len(list))
