import string

def rot18(teks):
    # Tabel translasi untuk huruf dengan ROT13
    rot13_table = str.maketrans(
        string.ascii_uppercase + string.ascii_lowercase,
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    )
    # Tabel translasi untuk digit dengan ROT5
    rot5_table = str.maketrans("0123456789", "5678901234")
    
    # Terapkan ROT13 untuk huruf
    hasil = teks.translate(rot13_table)
    # Terapkan ROT5 untuk digit
    hasil = hasil.translate(rot5_table)
    return hasil

def rot18_verbose(teks):
    result = ""
    for char in teks:
        if char.isalpha():
            converted = rot18(char)
            print(f"{char} -> {converted}")
            result += converted
        elif char.isdigit():
            converted = rot18(char)
            print(f"{char} -> {converted}")
            result += converted
        else:
            print(f"{char} tidak diubah")
            result += char
    return result

# Latihan 2: Antarmuka CLI untuk menerima input teks
teks = input("Masukkan teks untuk ROT18: ")

# Latihan 3: Validasi agar input tidak kosong
if teks.strip() == "":
    print("Input tidak boleh kosong!")
    exit()

# Latihan 1: Pastikan fungsi hanya mengubah huruf dan digit
cipher = rot18(teks)
print("Hasil ROT18:", cipher)

# Latihan 4: Tampilkan perbandingan tiap karakter sebelum dan sesudah ROT18
print("Verbose ROT18:")
print(rot18_verbose(teks))