import brotli

def brotli_compress(data):
    return brotli.compress(data.encode())

data = input("Compress payload using Brotli: ")
compressed = brotli_compress(data)
print(f"Brotli Compressed: {compressed}")