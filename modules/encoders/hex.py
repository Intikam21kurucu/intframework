def hex_encode(data):
    return data.encode().hex()

data = input("Encode payload in Hex: ")
encoded = hex_encode(data)
print(f"Hex Encoded: {encoded}")