n = int(input())
c = 0
for i in range(0, n):
    x, y = list(map(int, input().split()))
    if abs(x-y) >= 2:
        c += 1
print(c)
