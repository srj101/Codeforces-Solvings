n, k = map(int, input().split())
members = list(map(int, input().split()))
for i in members:
    if i > 5-k:
        n -= 1
print(n//3)
