def caesar_encrypt(teks, pergeseran):
    hasil = ""
    for char in teks:
        if char.isalpha():  # Latihan 1: Pastikan hanya huruf yang diubah
            basis = 65 if char.isupper() else 97
            hasil += chr((ord(char) - basis + pergeseran) % 26 + basis)
        else:
            hasil += char
    return hasil

def caesar_decrypt(teks, pergeseran):
    return caesar_encrypt(teks, -pergeseran)

def caesar_verbose(teks, pergeseran):
    hasil = ""
    for char in teks:
        if char.isalpha():
            basis = 65 if char.isupper() else 97
            shifted_val = (ord(char) - basis + pergeseran) % 26 + basis
            print(f"{char} ({ord(char)}) -> {chr(shifted_val)} ({shifted_val})")  # Latihan 4: Tampilkan langkah pergeseran
            hasil += chr(shifted_val)
        else:
            print(f"{char} tidak diubah")
            hasil += char
    return hasil

# Latihan 2: Antarmuka CLI untuk enkripsi atau dekripsi
mode = input("Ketik 'e' untuk enkripsi atau 'd' untuk dekripsi: ").lower()
pergeseran = int(input("Masukkan nilai pergeseran (maksimal 25): "))

# Latihan 3: Validasi nilai pergeseran
if pergeseran > 25:
    print("Nilai pergeseran maksimal adalah 25.")
    exit()

text_input = input("Masukkan pesan: ")

if mode == 'e':
    encrypted = caesar_encrypt(text_input, pergeseran)
    print("Pesan terenkripsi:", encrypted)
    print("Verbose shift:")
    caesar_verbose(text_input, pergeseran)
elif mode == 'd':
    decrypted = caesar_decrypt(text_input, pergeseran)
    print("Pesan didekripsi:", decrypted)
    print("Verbose shift:")
    caesar_verbose(text_input, -pergeseran)
else:
    print("Mode tidak valid")