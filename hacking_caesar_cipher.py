message = 'GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol.upper() in LETTERS:
            num = LETTERS.find(symbol.upper())
            num = (num - key) % len(LETTERS)
            translated += LETTERS[num] if symbol.isupper() else LETTERS[num].lower()
        else:
            translated += symbol
    print(f'Hacking key #{key}: {translated}')
