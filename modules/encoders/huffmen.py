import heapq

def huffman_encoding(data):
    freq = {char: data.count(char) for char in set(data)}
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huff_dict = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
    huff_dict = {item[0]: item[1] for item in huff_dict}
    return ''.join(huff_dict[char] for char in data)

data = input("Encode payload using Huffman encoding: ")
encoded = huffman_encoding(data)
print(f"Huffman Encoded: {encoded}")