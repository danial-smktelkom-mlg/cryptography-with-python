import string

ALPHABET = string.ascii_uppercase

def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext.upper():
        if char in ALPHABET:
            index = ALPHABET.index(char)
            encrypted_index = (index * key) % 26
            ciphertext += ALPHABET[encrypted_index]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    inverse_key = None
    for i in range(26):
        if (i * key) % 26 == 1:
            inverse_key = i
            break
    if inverse_key is None:
        return 'Error: Key is not valid.'
    for char in ciphertext.upper():
        if char in ALPHABET:
            index = ALPHABET.index(char)
            decrypted_index = (index * inverse_key) % 26
            plaintext += ALPHABET[decrypted_index]
        else:
            plaintext += char
    return plaintext

plaintext = 'HELLO WORLD'
key = 7
ciphertext = encrypt(plaintext, key)
print('Plaintext:', plaintext)
print('Key:', key)
print('Ciphertext:', ciphertext)
print('Decrypted text:', decrypt(ciphertext, key))
