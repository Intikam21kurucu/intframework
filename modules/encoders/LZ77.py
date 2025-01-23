import zlib

def lz77_compress(data):
    return zlib.compress(data.encode())

data = input("Compress payload using LZ77 (zlib): ")
compressed = lz77_compress(data)
print(f"LZ77 Compressed: {compressed}")