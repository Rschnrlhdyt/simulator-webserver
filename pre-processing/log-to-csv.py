# Mengubah .log ke .csv
import csv
from datetime import datetime

# Ganti path_file_log dengan path file teks yang sesuai
path_file_txt = 'path:\\folder\\input.log'

# Ganti path_file_csv dengan path file CSV yang dihasilkan
path_file_csv = 'path:\\folder\\output.csv'

# Nama kolom yang diinginkan
column_names = ["ip_address", "timestamp", "request_method", "path", "status_code", "response_size", "referrer", "user_agent"]

with open(path_file_txt, 'r') as file_txt, open(path_file_csv, 'w', newline='') as file_csv:
    csv_writer = csv.writer(file_csv)
    csv_writer.writerow(column_names)

    for line in file_txt:
        # Pisahkan setiap elemen dalam baris menggunakan spasi
        elements = line.strip().split()

        # Pastikan jumlah elemen mencukupi sebelum mencoba mengakses indeks tertentu
        if len(elements) >= 12:
            ip_address = elements[0]
            timestamp_str = f"{elements[3]} {elements[4]}"
            timestamp = datetime.strptime(timestamp_str, "[%d/%b/%Y:%H:%M:%S %z]")
            request_method = elements[5][1:] if elements[5] != '"-"' else ""
            path = elements[6] if elements[6] != '"-"' else ""
            status_code = elements[8]
            response_size = elements[9]
            referrer = elements[10] if elements[10] != '"-"' else ""
            user_agent = " ".join(elements[11:]) if len(elements) > 11 else ""

            # Tulis baris baru ke file CSV
            csv_writer.writerow([ip_address, timestamp, request_method, path, status_code, response_size, referrer, user_agent])
        else:
            print(f"Jumlah elemen dalam baris tidak mencukupi: {line}")

print(f"File CSV berhasil dibuat: {path_file_csv}")