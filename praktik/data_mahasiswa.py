
# Program Praktik: Pengelolaan Data Mahasiswa
# Nama: Farid Syahputra
# NIM: 2225250222
# Kelas: 3F

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim)


# Fungsi untuk menghitung rata-rata nilai mahasiswa
def hitung_rata_rata(data):
    if not data:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)


# 1. Menampilkan data mahasiswa berdasarkan NIM
print("=== PENCARIAN MAHASISWA ===")
nim_dicari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_dicari)

if hasil:
    print("NIM:", nim_dicari)
    print("Nama:", hasil["nama"])
    print("Kelas:", hasil["kelas"])
    print("Nilai:", hasil["nilai"])
else:
    print("Data tidak ditemukan")


# 2. Menguji pencarian NIM yang tidak tersedia
print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")
nim_dicari = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim_dicari)

if hasil:
    print(hasil)
else:
    print("Data tidak ditemukan")


# 3. Menambahkan data mahasiswa baru
print("\n=== MENAMBAHKAN MAHASISWA ===")
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}
print("Data mahasiswa A006 berhasil ditambahkan.")


# 4. Mengubah nilai mahasiswa
print("\n=== MENGUBAH NILAI ===")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai Budi berhasil diubah menjadi 82.")


# 5. Menampilkan seluruh data mahasiswa menggunakan items()
print("\n=== SELURUH DATA MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(f"NIM   : {nim}")
    print(f"Nama  : {info['nama']}")
    print(f"Kelas : {info['kelas']}")
    print(f"Nilai : {info['nilai']}")
    print("-" * 25)


# 6. Menghitung rata-rata nilai mahasiswa
print("=== RATA-RATA NILAI ===")
rata_rata = hitung_rata_rata(data_mahasiswa)
print(f"Rata-rata nilai: {rata_rata:.2f}")
