def xor_encode(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

data = input("Encode payload in XOR: ")
key = int(input("Enter XOR key: "))
encoded = xor_encode(data, key)
print(f"XOR Encoded: {encoded}")