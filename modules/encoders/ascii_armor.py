def ascii_armoring(data):
    return ''.join(format(ord(i), '08b') for i in data)

data = input("Encode payload using ASCII Armoring: ")
encoded = ascii_armoring(data)
print(f"ASCII Armored: {encoded}")