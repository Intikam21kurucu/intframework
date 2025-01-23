import base64

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

data = input("Enter the text to encode with Base64: ")
encoded = base64_encode(data)
print(f"Base64 Encoded: {encoded}")