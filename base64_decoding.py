import base64

encoded_data = b"RW5jb2RlIHRoaXMgdGV4dA=="
decoded_data = base64.b64decode(encoded_data)

print("Decoded text is:")
print(decoded_data.decode("utf-8"))
