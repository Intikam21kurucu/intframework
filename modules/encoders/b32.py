import base64

def base32_encode(data):
    return base64.b32encode(data.encode()).decode()

data = input("Encode payload in Base32: ")
encoded = base32_encode(data)
print(f"Base32 Encoded: {encoded}")