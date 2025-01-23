def zigzag_encode(data):
    return ''.join(data[i] if i % 2 == 0 else data[i][::-1] for i in range(len(data)))

data = input("Encode payload using Zigzag encoding: ")
encoded = zigzag_encode(data)
print(f"Zigzag Encoded: {encoded}")