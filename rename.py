import os

image_directory = "C:/Users/ilker/Desktop/pnomoni/"

# Klasördeki dosyaları sıralı olarak al
file_list = sorted(os.listdir(image_directory))

# Görüntüleri sırasıyla yeniden adlandır
for i, file_name in enumerate(file_list, 1):
    # Dosya uzantısını al
    file_ext = os.path.splitext(file_name)[1]

    # Yeni dosya adını oluştur
    new_file_name = "goruntu_" +str(i) + file_ext

    # Eski ve yeni dosya yollarını oluştur
    old_file_path = os.path.join(image_directory, file_name)
    new_file_path = os.path.join(image_directory, new_file_name)

    # Dosyayı yeniden adlandır
    os.rename(old_file_path, new_file_path)

print("Görüntüler başarıyla yeniden adlandırıldı.")
