import csv

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
    import os
    os.replace(temp_file, csv_file)

# CSV dosyasının adı ve boşlukları kaldırmak istediğiniz sütunun indeksi
csv_file = 'berrin.csv'
column_index = 2  # Örnek olarak 2. sütun

remove_blank(csv_file, column_index)
