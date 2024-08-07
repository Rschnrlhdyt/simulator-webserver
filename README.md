# Simulator Web Server

Web Server Simulator adalah alat yang digunakan untuk mensimulasikan permintaan web server dengan menggunakan pustaka [simpy](https://www.sympy.org/en/docs.html). Simulator ini memungkinkan Anda untuk mensimulasikan berbagai jenis web server. Simulasi ini dapat digunakan untuk menganalisis berbagai aspek performa web server seperti distribusi status kode, metode permintaan, dan referer.

## Fitur

- Simulasi permintaan ke web server.
- Visualisasi hasil simulasi dalam bentuk grafik dan diagram pie.

## Cara Penggunaan

1. Pastikan Anda memiliki Python dan `pip` terinstal.
2. Pastikan Anda memiliki `virtualenv` terpasang. Anda dapat menginstallnya menggunakan `pip` melalui command prompt.

    ```bash
    pip install virtualenv
    ```
   Buat virtual environment di dalam direktori proyek Anda.

    ```bash
    virtualenv venv
    ```
   Aktifkan virtual environment yang baru saja dibuat. Cara mengaktifkannya tergantung pada sistem operasi yang Anda gunakan:
   - Windows
     ```bash
     \venv\Scripts\activate
     ```
   - MacOs/Linux
     ```bash
     source venv\bin\activate
     ```
4. Instal pustaka yang diperlukan dengan menjalankan perintah berikut:

    ```bash
    pip install -r requirements.txt
    ```
   Jalankan jupyter notebook
    ```bash
    jupyter notebook
    ```
6. Jalankan program pada folder pre-processing dengan urutan:
    - `log-to-csv`: mengubah file format .log menjadi .csv
    - `cleaning-data`: melakukan pembersihan entri pada file
    - `menghitung-interval-arrival`: menghitung interval arrival request dari file
    - `distribusi-requests-per-jam`: mencari distribusi data rata-rata permintaan per jam
    - `distribusi-interval`: mencari distribusi interval permintaan
    - `distribusi-status-code`: mencari distribusi status code
    - `distribusi-requests-method`: mencari distribusi requests method
7. Setelah mendapatkan distribusi data untuk setiap variabel yang akan digunakan, tambahkan distribusi data tersebut ke dalam cell `simulator`
8. Parameter simulasi yang dapat diubah untuk menguji kinerja web server yaitu:
    - num_server
    - simulation_duration_days
    - lambda
9. Jalankan simulator
