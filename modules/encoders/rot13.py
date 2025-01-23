def rot13_encode(data):
    return data.translate(str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
                                        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))

data = input("Encode payload in ROT13: ")
encoded = rot13_encode(data)
print(f"ROT13 Encoded: {encoded}")