def vowel_stripping_encode(data):
    return ''.join(char for char in data if char.lower() not in 'aeiou')

data = input("Encode payload by stripping vowels: ")
encoded = vowel_stripping_encode(data)
print(f"Vowel Stripped: {encoded}")