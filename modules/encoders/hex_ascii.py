def hex_ascii_encode(data):
    return ' '.join(format(ord(char), 'x') for char in data)

data = input("Encode payload using Hexadecimal ASCII: ")
encoded = hex_ascii_encode(data)
print(f"Hexadecimal ASCII Encoded: {encoded}")