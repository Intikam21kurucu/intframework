import base64
def b64url_encode(data):
    return base64.urlsafe_b64encode(data.encode()).decode()

data = input("Encode payload in Base64 URL format: ")
encoded = b64url_encode(data)
print(f"B64URL Encoded: {encoded}")