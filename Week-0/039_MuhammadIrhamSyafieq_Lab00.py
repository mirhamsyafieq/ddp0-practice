# import library math untuk menggunakan nilai pi dan akar kuadrat
import math

print("=" * 60)
print("SELAMAT DATANG DI SISTEM PENCATATAN PENDUDUK FLORIAN!")
print("=" * 60)
print("\n====== Data Penduduk ======")

# menyimpan data penduduk yang di-input oleh pengguna
nama = input("Nama : ")
tempat_lahir = input("Tempat Lahir : ")
tanggal_lahir = input("Tanggal Lahir : ")
spesies = input("Spesies : ")
tinggi = float(input("Tinggi badan (dalam m) : "))
berat = float(input("Berat badan (dalam kg) : "))

# menghitung tinggi dan luas rumah berdasarkan rumus pada soal
tinggi_rumah = round(tinggi + 0.85, 2)
luas_rumah = round((math.pi * math.sqrt(2) * (tinggi ** 2)) + (berat / 3), 2)

print("\n====== Ringkasan Data Penduduk ======")
print(
    f"Penduduk berspesies {spesies} dengan nama {nama} "
    f"yang lahir tanggal {tanggal_lahir} di {tempat_lahir} "
    f"berhasil terdaftar menjadi penduduk negeri Florian!"
)
print(
    f"{nama} berhak atas rumah dengan tinggi {tinggi_rumah} meter "
    f"dan luas {luas_rumah} meter persegi."
)

print("=" * 60)
print("TERIMA KASIH SUDAH MELAKUKAN PENCATATAN DATA PENDUDUK!")
print("=" * 60)
