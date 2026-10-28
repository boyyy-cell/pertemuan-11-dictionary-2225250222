
# Latihan 3: Manipulasi Dictionary

mahasiswa = {
    "nama": "Farid",
    "kelas": "3F",
    "nilai": 80
}

print("Data awal:", mahasiswa)

# Menambahkan data
mahasiswa["nim"] = "2225250222"
print("Setelah menambah NIM:", mahasiswa)

# Mengubah data
mahasiswa["nilai"] = 90
print("Setelah mengubah nilai:", mahasiswa)

# Menghapus data
mahasiswa.pop("kelas")
print("Setelah menghapus kelas:", mahasiswa)
