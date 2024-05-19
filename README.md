# Simulator Web Server

Web Server Simulator adalah alat yang digunakan untuk mensimulasikan permintaan web server dengan menggunakan pustaka [simpy](https://www.sympy.org/en/docs.html). Simulator ini memungkinkan Anda untuk mensimulasikan berbagai jenis web server. Simulasi ini dapat digunakan untuk menganalisis berbagai aspek performa web server seperti distribusi status kode, metode permintaan, dan referer.

## Fitur

- Simulasi permintaan ke web server.
- Dukungan untuk berbagai jenis web server.
- Visualisasi hasil simulasi dalam bentuk grafik dan diagram pie.

## Cara Penggunaan

1. Pastikan Anda memiliki Python dan `pip` terinstal. Disarankan untuk menjalankan kode di jupyter notebook.
2. Instal pustaka yang diperlukan dengan menjalankan perintah berikut:

    ```bash
    pip install simpy numpy matplotlib networkx scipy
    ```
3. Jalankan program pada folder pre-processing dengan urutan:
    - `log-to-csv.py`: mengubah file format .log menjadi .csv
    - `cleaning-data.py`: melakukan pembersihan entri pada file
    - `menghitung-interval-arrival.py`: menghitung interval arrival request dari file
    - `distribusi-requests-per-jam.py`: mencari distribusi data rata-rata permintaan per jam
    - `distribusi-interval.py`: mencari distribusi interval permintaan
    - `distribusi-status-code.py`: mencari distribusi status code
    - `distribusi-requests-method.py`: mencari distribusi requests method
4. Setelah mendapatkan distribusi data untuk setiap variabel yang akan digunakan, tambahkan distribusi data tersebut ke dalam file `simulator_webserver.py`
5. Parameter simulasi yang dapat diubah untuk menguji kinerja web server yaitu:
    - num_server
    - simulation_duration_days
    - lambda
6. Jalankan simulator
