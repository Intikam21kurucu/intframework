import random

def shift_encode(data):
    shift = random.randint(1, 10)
    return ''.join(chr(ord(c) + shift) for c in data)

data = input("Encode payload with character shifting: ")
encoded = shift_encode(data)
print(f"Shift Encoded: {encoded}")