def truncated_base64_encode(data):
    return base64.b64encode(data.encode()).decode()[:10]

data = input("Encode payload using truncated Base64: ")
encoded = truncated_base64_encode(data)
print(f"Truncated Base64 Encoded: {encoded}")