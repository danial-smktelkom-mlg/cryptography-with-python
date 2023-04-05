import base64

def xor_cipher(plaintext, key):
    ciphertext_bytes = bytearray()
    for i in range(len(plaintext)):
        key_byte = key[i % len(key)]
        ciphertext_byte = plaintext[i] ^ ord(key_byte)
        ciphertext_bytes.append(ciphertext_byte)
    return base64.b64encode(ciphertext_bytes).decode('utf-8')

def xor_decipher(ciphertext, key):
    ciphertext_bytes = base64.b64decode(ciphertext)
    plaintext_bytes = bytearray()
    for i in range(len(ciphertext_bytes)):
        key_byte = key[i % len(key)]
        plaintext_byte = ciphertext_bytes[i] ^ ord(key_byte)
        plaintext_bytes.append(plaintext_byte)
    return plaintext_bytes.decode('utf-8')

plaintext = "XOR procedure"
key = "awesomepassword"
print("Plaintext:", plaintext)
ciphertext = xor_cipher(plaintext.encode('utf-8'), key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = xor_decipher(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
