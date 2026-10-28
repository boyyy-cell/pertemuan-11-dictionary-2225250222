
# Latihan 6: Fungsi Dictionary

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92}
}


def cari_mahasiswa(data, nim):
    return data.get(nim)


def hitung_rata_rata(data):
    if not data:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)


print("Hasil Pencarian:")
print(cari_mahasiswa(mahasiswa, "A003"))

print("\nRata-rata Nilai:")
print(f"{hitung_rata_rata(mahasiswa):.2f}")
