message = 'fxgvbimtdtgixfuxetctktgbghotmbyuxkutlblmxdghehzbrtgzfxgwhkhgzlblptfxfbebdbdhfixmxglbtutw21'
translated = ''
i = len(message) - 1

while i >= 0:
    translated += message[i]
    i -= 1

print("The plain text is:", message)
print("The cipher text is:", translated)
