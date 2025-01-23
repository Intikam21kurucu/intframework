import base64
def base16_encode(data):
    return base64.b16encode(data.encode()).decode()

data = input("Encode payload in Base16: ")
encoded = base16_encode(data)
print(f"Base16 Encoded: {encoded}")