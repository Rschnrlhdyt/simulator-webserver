#cleaning data
import pandas as pd

# Membaca file CSV
csv_file_path = 'path:\\folder\\output.csv'
df = pd.read_csv(csv_file_path)

# Menampilkan informasi umum tentang data
print("Info sebelum data cleaning:")
print(df.info())

# Menghapus duplikat (jika ada)
df = df.drop_duplicates()

# Menangani nilai-nilai yang hilang
df = df.dropna()

# Mengonversi kolom timestamp menjadi tipe data datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')

# Menyimpan kembali ke file CSV setelah data cleaning
cleaned_csv_path = 'path:\\folder\\cleaning\\output.csv'
df.to_csv(cleaned_csv_path, index=False)

# Menampilkan informasi setelah data cleaning
print("\nInfo setelah data cleaning:")
print(df.info())