import hashlib
def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

data = input("Hash payload using MD5: ")
hashed = md5_hash(data)
print(f"MD5 Hashed: {hashed}")