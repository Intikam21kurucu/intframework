def num_to_char_mapping_encode(data):
    return ' '.join(str(ord(char)) for char in data)

data = input("Encode payload using number-to-character mapping: ")
encoded = num_to_char_mapping_encode(data)
print(f"Number-to-Character Encoded: {encoded}")