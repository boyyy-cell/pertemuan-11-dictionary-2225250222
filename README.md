
# Pertemuan 11 — Dictionary/Map Python

## Identitas Mahasiswa
- Nama: Farid Syahputra
- NIM: 2225250222
- Kelas: 3F
- Program Studi: S1 Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan
1. Memahami konsep dictionary pada Python.
2. Mempraktikkan akses, penambahan, perubahan, dan penghapusan data.
3. Memahami iterasi dictionary dan dictionary bersarang.
4. Menggunakan fungsi untuk mengolah data mahasiswa.

## Struktur Folder
```text
pertemuan-11-dictionary-2225250222/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Struktur Data
Program menggunakan dictionary dengan NIM sebagai key. Setiap NIM memiliki dictionary bersarang yang berisi nama, kelas, dan nilai mahasiswa.

## Cara Menjalankan
Buka terminal pada folder proyek, lalu jalankan:

```bash
python praktik/data_mahasiswa.py
```

## Pengujian Program

| No. | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Mencari NIM A003 | Data Citra ditemukan |
| 2 | Mencari NIM A999 | Data tidak ditemukan |
| 3 | Menambahkan NIM A006 | Data Fajar berhasil ditambahkan |
| 4 | Mengubah nilai A002 | Nilai menjadi 82 |
| 5 | Menampilkan seluruh data | Semua data mahasiswa tampil |
| 6 | Menghitung rata-rata | Rata-rata tampil dengan 2 angka desimal |

## Refleksi
Saat mengakses dictionary, penggunaan key yang tidak tersedia dapat menyebabkan KeyError jika menggunakan tanda kurung siku secara langsung. Untuk menghindarinya, fungsi get() dapat digunakan agar program memberikan nilai None atau nilai default jika key tidak ditemukan. Dengan demikian, program lebih aman saat mencari data mahasiswa yang belum tersedia.
