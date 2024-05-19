# Melihat distribusi interval arrival
import pandas as pd

# Daftar nama file CSV
file_paths = ['path:\\folder\\cleaning\\output.csv',
             'path:\\folder\\cleaning\\output2.csv',
             'path:\\folder\\cleaning\\output3.csv']
# Ganti dengan path ke masing-masing file CSV Anda

# Membaca data dari setiap file dan menggabungkannya
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path, low_memory=False)
    dfs.append(df)

combined_df = pd.concat(dfs)

# Menghitung jumlah total data
total_data = len(combined_df)

# Menghitung jumlah permintaan dan persentasenya untuk setiap interval kedatangan
interval_counts = combined_df['interval_arrival'].value_counts()

# Menghitung rata-rata permintaan
average_requests = total_data / len(interval_counts)

print("Interval Arrival\tJumlah Permintaan\tPersentase")
print("-------------------------------------------------")
for interval, count in interval_counts.items():
    percentage = (count / total_data) * 100
    print(f"{interval}\t\t\t{count}\t\t\t{percentage:.2f}%")