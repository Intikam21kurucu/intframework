def reverse_encode(data):
    return data[::-1]

data = input("Encode payload by reversing the string: ")
encoded = reverse_encode(data)
print(f"Reversed Encoded: {encoded}")