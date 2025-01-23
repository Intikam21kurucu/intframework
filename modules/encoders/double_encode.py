import base64
def double_encode(data):
    return base64.b64encode(base64.b64encode(data.encode()).decode().encode()).decode()

data = input("Double encode payload: ")
encoded = double_encode(data)
print(f"Double Encoded: {encoded}")