def reverse_and_ascii_encode(data):
    return ' '.join(str(ord(char)) for char in data[::-1])

data = input("Reverse and encode payload with ASCII values: ")
encoded = reverse_and_ascii_encode(data)
print(f"Reversed and ASCII Encoded: {encoded}")