# recommendation-system-product

## Gambaran Umum
Repositori: https://github.com/Fahmifc123/recommendation-system-product

Akses URL Online : https://recommendation-system-appuct-j9ytm7xcndkvdgi29aydj5.streamlit.app

Repositori ini berisi kode sumber dan dokumentasi untuk aplikasi AI berbasis web yang memberikan rekomendasi produk menggunakan K-Means Clustering. Aplikasi ini dirancang untuk memberikan rekomendasi produk kepada pengguna berdasarkan perilaku dan preferensi mereka.

## Komponen Utama
- Eksplorasi Data: Proses eksplorasi data melibatkan analisis data pelanggan dan produk. Temuan kunci mencakup distribusi produk di seluruh kategori, preferensi pelanggan, dan ringkasan statistik dataset.
- Pengembangan Model: Inti dari aplikasi adalah model K-Means Clustering, yang mengelompokkan pelanggan berdasarkan perilaku pembelian mereka. Model ini dilatih pada data historis untuk mengidentifikasi pola dan kesamaan di antara pelanggan.
- Pengembangan Aplikasi Web: Aplikasi web dibangun menggunakan Streamlit, sebuah perpustakaan Python untuk membuat aplikasi web interaktif. Pengguna dapat memasukkan ID pelanggan mereka, dan aplikasi akan memberikan rekomendasi produk teratas.
- Implementasi: Aplikasi diimplementasikan di platform cloud, dan pengguna dapat mengaksesnya melalui antarmuka web. Implementasi memastikan bahwa aplikasi dapat diakses oleh audiens yang lebih luas.

## Struktur Kode Sumber
Kode sumber diorganisir sebagai berikut:
- app.py: File ini berisi kode utama untuk aplikasi web Streamlit. Ini menangani input pengguna, melakukan inferensi model, dan menampilkan rekomendasi.
- kmeans_model.pkl: File ini berisi model K-Means Clustering yang telah diserialkan, memungkinkan untuk pengambilan dan inferensi yang mudah.
- data_baru.csv: Dataset yang digunakan untuk melatih model dan memberikan rekomendasi.

## Cara Menjalankan Aplikasi Secara Lokal
Untuk menjalankan aplikasi rekomendasi produk secara lokal, ikuti langkah-langkah berikut:
Clone Repositori:
```
- git clone https://github.com/Fahmifc123/recommendation-system-product
- cd recommendation-system-product
- pip install -r requirements.txt
```

Jalankan Aplikasi: ```streamlit run app.py```
Akses Aplikasi Web:
- Buka URL yang disediakan di browser web Anda, dan Anda akan melihat halaman utama aplikasi rekomendasi produk.
- Masukkan ID pelanggan yang valid dalam kolom input teks dan tekan Enter.
- Lihat Rekomendasi: Aplikasi akan menampilkan 3 rekomendasi produk teratas untuk ID pelanggan yang dimasukkan.
