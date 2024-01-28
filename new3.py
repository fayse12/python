import os
import csv

def remove_blank_from_csv_files(folder_path, column_index):
    # Klasördeki tüm dosyaları listeler
    files = os.listdir(folder_path)
    
    # Her bir dosya için işlem yap
    for file_name in files:
        if file_name.endswith('.csv'):  # Sadece CSV dosyalarını işle
            file_path = os.path.join(folder_path, file_name)
            remove_blank(file_path, column_index)

def remove_blank(csv_file, column_index):
    # Yeni CSV dosyasını yazmak için geçici bir dosya oluşturun
    temp_file = csv_file.replace('.csv', '_temp.csv')

    with open(csv_file, 'r', newline='') as infile, \
         open(temp_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row:  # Satır boş değilse
                # Belirli sütundaki veriyi alın ve satır boşluklarını silin
                row[column_index] = row[column_index].replace('\n', '')
            writer.writerow(row)

    # Geçici dosyayı orijinal dosya ile değiştirin
    os.replace(temp_file, csv_file)

# Klasör yolunu ve boşlukları kaldırmak istediğiniz sütunun indeksini belirtin
folder_path = "C:/Users/berri/OneDrive/Masaüstü/Yeni/csvs"
column_index = 2  # Örnek olarak 2. sütun

remove_blank_from_csv_files(folder_path, column_index)

