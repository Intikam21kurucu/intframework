def reverse_base64_encode(data):
    reversed_data = data[::-1]
    return base64.b64encode(reversed_data.encode()).decode()

data = input("Encode payload with reversed Base64: ")
encoded = reverse_base64_encode(data)
print(f"Reversed Base64 Encoded: {encoded}")