def char_shift_encode(data, shift):
    return ''.join(chr(ord(char) + shift) for char in data)

data = input("Encode payload using character shift: ")
shift = int(input("Enter shift value: "))
encoded = char_shift_encode(data, shift)
print(f"Character Shift Encoded: {encoded}")