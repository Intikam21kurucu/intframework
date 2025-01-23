import html

def html_entity_encode(data):
    return html.escape(data)

data = input("Encode payload using HTML entities: ")
encoded = html_entity_encode(data)
print(f"HTML Entity Encoded: {encoded}")