# Melihat distribusi status code domain
import pandas as pd
import os
import matplotlib.pyplot as plt

# Daftar nama file CSV
file_paths = ['path:\\folder\\cleaning\\output.csv',
             'path:\\folder\\cleaning\\output2.csv',
             'path:\\folder\\cleaning\\output3.csv'
              ]
# Ganti dengan path ke masing-masing file CSV Anda

# Membaca data dari setiap file dan menggabungkannya menjadi satu DataFrame
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# Menghitung jumlah keseluruhan status code dalam gabungan semua file
total_status_codes = len(combined_df['status_code'])

# Menghitung jumlah masing-masing status code
status_code_counts = combined_df['status_code'].value_counts()

# Menghitung persentase masing-masing status code
status_code_percentages = {}
for status_code, count in status_code_counts.items():
    percentage = (count / total_status_codes) * 100
    status_code_percentages[status_code] = percentage
    
# Menampilkan hasil
print("Status Code:")
for status_code, percentage in status_code_percentages.items():
    print(f"{status_code}: {percentage:.2f}%")

# Filter status code yang valid
valid_status_codes = {str(code): count for code, count in status_code_counts.items() if isinstance(code, int)}

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(valid_status_codes.values(), startangle=140)
plt.title('Status Code\n tanggal - tanggal')
plt.axis('equal')  # Ensure the pie is drawn as a circle

# Add legend
legend_texts = [f"{status_code}: {count} ({percentage:.2f}%)"
                for status_code, count, percentage in zip(valid_status_codes.keys(),
                                                            valid_status_codes.values(),
                                                            status_code_percentages.values())]
plt.legend(legend_texts, loc='lower left')

# Show the plot
plt.show()