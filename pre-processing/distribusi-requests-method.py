# Melihat persentase request method
import pandas as pd
import os
import matplotlib.pyplot as plt

# Daftar nama file CSV
file_paths = ['path:\\folder\\cleaning\\output.csv',
             'path:\\folder\\cleaning\\output2.csv',
             'path:\\folder\\cleaning\\output3.csv']
# Ganti dengan path ke masing-masing file CSV Anda

# Membaca data dari setiap file dan menggabungkannya menjadi satu DataFrame
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# Filter hanya method request yang valid (GET, POST, HEAD, OPTIONS)
valid_request_methods = ['GET', 'POST', 'HEAD', 'OPTIONS'] #sesuaikan dengan distribusi data Anda
combined_df = combined_df[combined_df['request_method'].isin(valid_request_methods)]

# Menghitung jumlah keseluruhan request method yang valid
total_request_method = len(combined_df)

# Menghitung jumlah masing-masing request method
request_method_counts = combined_df['request_method'].value_counts()

# Menghitung persentase masing-masing request method
request_method_percentages = {}
for request_method, count in request_method_counts.items():
    percentage = (count / total_request_method) * 100
    request_method_percentages[request_method] = percentage

# Plot pie chart untuk request method
plt.figure(figsize=(8, 8))
plt.pie(request_method_counts, startangle=140)
plt.title('Request Method\n tanggal - tanggal')
plt.axis('equal')  # Ensure the pie is drawn as a circle

# Add legend
legend_texts = [f"{method}: {count} ({percentage:.2f}%)"
                for method, count, percentage in zip(request_method_counts.index,
                                                      request_method_counts.values,
                                                      request_method_percentages.values())]
plt.legend(legend_texts, loc='lower left')

# Show the plot
plt.show()