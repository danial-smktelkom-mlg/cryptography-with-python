import base64

text = "Encode this text"
encoded_data = base64.b64encode(text.encode("utf-8"))

print("Encoded text with base 64 is")
print(encoded_data.decode("utf-8"))
