x, y = map(int, input().split())
p = sorted(list(map(int, input().split())))

minDif = p[-1] - p[0]
i = 0
while i + x - 1 < y:
    minDif = min(minDif, p[i + x - 1] - p[i])
    i += 1
print(minDif)
