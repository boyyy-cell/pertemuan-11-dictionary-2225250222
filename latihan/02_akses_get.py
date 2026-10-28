
# Latihan 2: Mengakses Dictionary dengan get()

mahasiswa = {
    "nama": "Farid",
    "nim": "2225250222",
    "kelas": "3F"
}

print("Nama:", mahasiswa.get("nama"))
print("NIM:", mahasiswa.get("nim"))
print("Kelas:", mahasiswa.get("kelas"))

# Mengakses key yang tidak tersedia
print("Nilai:", mahasiswa.get("nilai", "Belum tersedia"))
