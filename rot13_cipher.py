def rot13(text):
    return text.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
    'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

def main():
    txt = "Hello, world!"
    print(rot13(txt))

if __name__ == "__main__":
    main()
