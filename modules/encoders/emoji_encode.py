def emoji_encode(data):
    emoji_dict = {'a': '😀', 'b': '😁', 'c': '😂', 'd': '🤣', 'e': '😃', 'f': '😄', 'g': '😅', 'h': '😆', 'i': '😇', 'j': '😈', 'k': '👿', 'l': '😻', 'm': '😼', 'n': '😽', 'o': '😋', 'p': '😜', 'q': '😝', 'r': '😛', 's': '😎', 't': '🤓', 'u': '🧐', 'v': '😕', 'w': '🙄', 'x': '😬', 'y': '😡', 'z': '😑'}
    return ''.join(emoji_dict.get(char, char) for char in data.lower())

data = input("Encode payload using Emojis: ")
encoded = emoji_encode(data)
print(f"Emoji Encoded: {encoded}")