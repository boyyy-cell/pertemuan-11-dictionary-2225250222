
# Latihan 4: Iterasi Dictionary

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92},
    "A004": {"nama": "Deni", "nilai": 74},
    "A005": {"nama": "Eka", "nilai": 88}
}

print("Daftar Mahasiswa:")

for nim, data in mahasiswa.items():
    print(f"NIM: {nim}")
    print(f"Nama: {data['nama']}")
    print(f"Nilai: {data['nilai']}")
    print("-" * 25)
