def vigenere_cipher(data, key):
    result = ''
    key = key.upper()
    for i, char in enumerate(data):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

data = input("Encode payload using Vigenère Cipher: ")
key = input("Enter Vigenère Cipher key: ")
encoded = vigenere_cipher(data, key)
print(f"Vigenère Cipher Encoded: {encoded}")