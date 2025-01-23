def unicode_encode(data):
    return ''.join(f"\\u{ord(c):04x}" for c in data)

data = input("Encode payload in Unicode: ")
encoded = unicode_encode(data)
print(f"Unicode Encoded: {encoded}")