def backslash_encode(data):
    return ''.join(f"\\{char}" for char in data)

data = input("Encode payload with backslashes: ")
encoded = backslash_encode(data)
print(f"Backslash Encoded: {encoded}")