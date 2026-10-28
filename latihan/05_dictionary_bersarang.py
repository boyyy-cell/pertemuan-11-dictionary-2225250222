
# Latihan 5: Dictionary Bersarang

mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    },
    "A002": {
        "nama": "Budi",
        "kelas": "A",
        "nilai": 78
    },
    "A003": {
        "nama": "Citra",
        "kelas": "B",
        "nilai": 92
    }
}

print("Data Mahasiswa:")
print("Nama:", mahasiswa["A001"]["nama"])
print("Kelas:", mahasiswa["A001"]["kelas"])
print("Nilai:", mahasiswa["A001"]["nilai"])

print("\nData Citra:")
print(mahasiswa["A003"])
