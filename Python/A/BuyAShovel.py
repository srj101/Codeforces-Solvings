x, y = map(int, input().split())
i = 1
while ((x*i) % 10) != 0 and ((x*i) % 10) != y:
    i += 1
print(i)
