import hashlib
def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

data = input("Hash payload using SHA-256: ")
hashed = sha256_hash(data)
print(f"SHA-256 Hashed: {hashed}")