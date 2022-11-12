import numpy as np

line1 = [26,29,27,28,30,34,29,31,36,39,37,35,42,39,42,40,43,44,48,49,47,48,48,55,48,49,55,48,54,55,59,60,58,61,64,63,63,64,64,66,69,64,69,71,75,71,75,78,72,73,78,78,80,81,81,82,78,84,89,87,87,89,90,94,]
line2 = [16,11,10,16,24,40,51,61,12,12,14,19,26,58,60,55,14,13,16,24,40,57,69,56,14,17,22,29,51,87,80,62,18,22,37,56,68,109,103,77,24,35,55,64,81,104,113,92,49,64,78,87,103,121,120,101,72,92,95,98,112,100,103,99,]
line3 = [12,13,14,18,27,44,54,53,14,13,14,20,35,46,58,59,13,15,18,26,40,64,63,62,16,18,25,38,56,74,80,71,20,27,39,50,74,91,95,86,34,41,54,70,85,106,105,97,53,64,75,86,100,107,110,104,71,77,89,98,100,112,106,102,]

# convert the line1 to 8*8
# line1 = np.array(line1)
# line1 = line1.reshape(8,8)
# print(line1)

with open('nicelemetablolari.txt') as f:
    lines = f.readlines()
    # her satırın sonuna , ekle ve yeni bir dosyaya kaydet
    lines = [line.strip() + ',' for line in lines]
    with open('nicelemetablolari2.txt', 'w') as f2:
        f2.writelines(lines)


print(len(line2))
# convert the line2 to 8*8 without np
line2 = [line2[i:i+8] for i in range(0, len(line2), 8)]
print(line2)


