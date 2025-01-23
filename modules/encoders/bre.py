def binary_representation_encode(data):
    return ' '.join(format(ord(char), '08b') for char in data)

data = input("Encode payload using binary representation: ")
encoded = binary_representation_encode(data)
print(f"Binary Representation Encoded: {encoded}")