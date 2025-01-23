import base58

def base58_encode(data):
    return base58.b58encode(data.encode()).decode()

data = input("Encode payload in Base58: ")
encoded = base58_encode(data)
print(f"Base58 Encoded: {encoded}")