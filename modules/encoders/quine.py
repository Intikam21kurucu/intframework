def quine_encode(data):
    return f'print({repr(data)})'

data = input("Encode payload using quine: ")
encoded = quine_encode(data)
print(f"Quine Encoded: {encoded}")