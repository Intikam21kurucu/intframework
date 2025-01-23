import urllib.parse

def url_encode(data):
    return urllib.parse.quote(data)

data = input("Encode payload in URL Encoding: ")
encoded = url_encode(data)
print(f"URL Encoded: {encoded}")