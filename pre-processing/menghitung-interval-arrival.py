# Menghitung dan menambahkan interval_arival ke file csv
import pandas as pd

# Membaca file CSV yang telah dibersihkan
csv_path = 'path:\\folder\\cleaning\\output.csv'
df = pd.read_csv(csv_path, low_memory=False)

# Mengkonversi kolom timestamp menjadi tipe data datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S%z')

# Mengurutkan DataFrame berdasarkan timestamp
df = df.sort_values(by='timestamp')

# Menghitung interval kedatangan dalam detik
df['interval_arrival'] = df['timestamp'].diff().dt.total_seconds()

# Menyimpan DataFrame yang telah diupdate ke file CSV dengan menambahkan kolom baru
df.to_csv(csv_path, index=False)