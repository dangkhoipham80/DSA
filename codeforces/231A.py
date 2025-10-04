n = int(input()) # n problems
ans = 0
for _ in range(n):
    a, b, c = map(int, input().split()) # read the whole line and map to each val
    if a + b + c >= 2:
        ans += 1
print(ans)

