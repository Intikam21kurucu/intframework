def caesar_cipher(data, shift):
    result = ''
    for char in data:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

data = input("Encode payload using Caesar Cipher: ")
shift = int(input("Enter Caesar Cipher shift: "))
encoded = caesar_cipher(data, shift)
print(f"Caesar Cipher Encoded: {encoded}")