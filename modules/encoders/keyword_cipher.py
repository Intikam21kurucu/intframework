def keyword_cipher_encode(data, keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    cipher_alphabet = ''.join(sorted(set(alphabet), key=alphabet.index))
    return ''.join(cipher_alphabet[(alphabet.index(char) + len(keyword)) % len(alphabet)] for char in data.lower())

data = input("Encode payload using keyword cipher: ")
keyword = input("Enter keyword for the cipher: ")
encoded = keyword_cipher_encode(data, keyword)
print(f"Keyword Cipher Encoded: {encoded}")