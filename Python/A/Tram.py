stops = int(input())
capacity = []
n = 0
for stop in range(0, stops):
    x, y = list(map(int, input().split()))
    n += y
    n -= x
    capacity.append(n)
print(max(capacity))
