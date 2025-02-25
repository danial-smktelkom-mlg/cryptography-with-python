import time

def reverse_cipher(pesan):
    cipher_text = ""
    i = len(pesan) - 1
    while i >= 0:
        cipher_text += pesan[i]
        i -= 1
    return cipher_text

def reverse_cipher_slicing(pesan):
    return pesan[::-1]

def reverse_cipher_verbose(pesan):
    cipher_text = ""
    i = len(pesan) - 1
    while i >= 0:
        print("Index:", i, "->", pesan[i])
        cipher_text += pesan[i]
        i -= 1
    return cipher_text

# Latihan 1: Menerima input dari pengguna
pesan_asli = input("Masukkan pesan untuk enkripsi: ")

# Latihan 2: Validasi input
if not isinstance(pesan_asli, str):
    print("Input harus berupa teks!")
    exit()

# Latihan 3: Versi fungsi menggunakan slicing
print("Cipher Text (slicing):", reverse_cipher_slicing(pesan_asli))

# Latihan 4: Fitur menampilkan indeks dan karakter yang diproses
print("Verbose Reverse Cipher:")
print(reverse_cipher_verbose(pesan_asli))

# Latihan 5: Catat waktu proses enkripsi
mulai = time.time()
cipher = reverse_cipher(pesan_asli)
selesai = time.time()

print("Pesan Asli   :", pesan_asli)
print("Cipher Text  :", cipher)
print("Waktu eksekusi: {:.6f} detik".format(selesai - mulai))