message = 'Odrzm sdqdmjqhorh'  # Pesan terenkripsi
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Ubah pesan menjadi huruf kapital
message = message.upper()

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = (LETTERS.find(symbol) - key) % len(LETTERS)  # Geser ke belakang dan lakukan wrap around
            translated += LETTERS[num]
        else:
            translated += symbol
    print(f"Hacking key #{key}: {translated}")