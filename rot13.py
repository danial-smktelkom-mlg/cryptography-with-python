import string

def rot13(teks):
    tabel_trans = str.maketrans(
        string.ascii_uppercase + string.ascii_lowercase,
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    )
    return teks.translate(tabel_trans)

def rot13_verbose(teks):
    result = ""
    for char in teks:
        if char.isalpha():
            converted = rot13(char)
            print(f"{char} -> {converted}")
            result += converted
        else:
            result += char
    return result

# Latihan 2: Antarmuka CLI untuk menerima input teks
teks = input("Masukkan teks untuk ROT13: ")

# Latihan 3: Validasi agar input tidak kosong
if teks.strip() == "":
    print("Input tidak boleh kosong!")
    exit()

# Latihan 1: Pastikan fungsi hanya mengubah huruf
cipher = rot13(teks)
print("Hasil ROT13:", cipher)

# Latihan 4: Tampilkan perbandingan tiap huruf sebelum dan sesudah ROT13
print("Verbose ROT13:")
print(rot13_verbose(teks))