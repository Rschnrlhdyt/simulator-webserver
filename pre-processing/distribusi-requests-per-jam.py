# Mencari rata-rata request per jam
import pandas as pd
import matplotlib.pyplot as plt

# Daftar nama file CSV
file_paths = ['path:\\folder\\cleaning\\output.csv',
             'path:\\folder\\cleaning\\output2.csv',
             'path:\\folder\\cleaning\\output3.csv']

# Membaca data dari setiap file dan menghitung jumlah permintaan per jam
requests_per_hour = {}
for i, file_path in enumerate(file_paths, start=1):
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    requests_per_hour[f'File_{i}'] = df.groupby('hour').size()

# Gabungkan data dari semua file
combined_requests = pd.concat(requests_per_hour.values(), axis=1).sum(axis=1)

# Hitung total permintaan gabungan
total_requests = combined_requests.sum()

# Hitung rata-rata permintaan per jam dari data gabungan
average_requests_per_hour = combined_requests / len(requests_per_hour)

# Hitung persentase permintaan per jam dari total permintaan
percentage_requests_per_hour = (combined_requests / total_requests) * 100

# Visualisasikan rata-rata permintaan per jam dalam bentuk histogram
plt.figure(figsize=(10, 6))
bars = plt.bar(average_requests_per_hour.index, average_requests_per_hour, color='skyblue', width=0.6)

plt.title('Rata-rata Permintaan per Jam Domain\n tanggal - tanggal')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Permintaan')
plt.grid(axis='y')

# Menambahkan keterangan jam di bawah setiap batang histogram
plt.gca().xaxis.set_ticks(range(len(average_requests_per_hour)))
plt.gca().xaxis.set_ticklabels(average_requests_per_hour.index)

# Menambahkan label di atas atau di dalam batang histogram
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 5, str(int(height)), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Visualisasikan persentase permintaan per jam dalam bentuk histogram
plt.figure(figsize=(10, 6))
bars = plt.bar(percentage_requests_per_hour.index, percentage_requests_per_hour, color='salmon', width=0.6)

plt.title('Persentase Permintaan per Jam\n tanggal - tanggal')
plt.xlabel('Jam')
plt.ylabel('Persentase Permintaan')
plt.grid(axis='y')

# Menambahkan keterangan jam di bawah setiap batang histogram
plt.gca().xaxis.set_ticks(range(len(percentage_requests_per_hour)))
plt.gca().xaxis.set_ticklabels(percentage_requests_per_hour.index)

# Menambahkan label di atas batang histogram
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()