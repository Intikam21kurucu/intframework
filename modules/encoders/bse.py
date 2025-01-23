def binary_string_encode(data):
    return ' '.join(format(ord(char), '08b') for char in data)

data = input("Encode payload using binary string encoding: ")
encoded = binary_string_encode(data)
print(f"Binary String Encoded: {encoded}")