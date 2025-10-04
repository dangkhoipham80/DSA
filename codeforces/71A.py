n = int(input())
for _ in range(n):
    w = input().strip()
    k = len(w)
    if k > 10:
        print(f"{w[0]}{k - 2}{w[k - 1]}")
    else:
        print(w)
