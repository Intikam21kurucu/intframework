def rle_encode(data):
    encoded = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoded.append(f"{data[i]}{count}")
        i += 1
    return ''.join(encoded)

data = input("Encode payload using Run-Length Encoding: ")
encoded = rle_encode(data)
print(f"RLE Encoded: {encoded}")