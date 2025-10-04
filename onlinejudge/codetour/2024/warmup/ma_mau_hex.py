import sys
from typing import Tuple

def hex_to_dec(s: str) -> int:
    return int(s, 16)

def parse_rgb(code: str) -> Tuple[int, int, int]:
    return hex_to_dec(code[1:3]), hex_to_dec(code[3:5]), hex_to_dec(code[5:7])

data = sys.stdin.read().strip().split()
n = int(data[0])
img1 = data[1:1+n]
img2 = data[1+n:1+2*n]

freq = {}
for a, b in zip(img1, img2):
    r1, g1, b1 = parse_rgb(a)
    r2, g2, b2 = parse_rgb(b)
    dR = (r2 - r1) % 256
    dG = (g2 - g1) % 256
    dB = (b2 - b1) % 256
    key = (dR, dG, dB)
    freq[key] = freq.get(key, 0) + 1

max_count = max(freq.values()) if freq else 0
percent = max_count * 100.0 / n
print(f"{percent:.2f}%")
