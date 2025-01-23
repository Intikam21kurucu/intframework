def skip_pattern_encode(data, skip=2):
    return ''.join(data[i] for i in range(0, len(data), skip))

data = input("Encode payload using skip pattern: ")
encoded = skip_pattern_encode(data)
print(f"Skip Pattern Encoded: {encoded}")