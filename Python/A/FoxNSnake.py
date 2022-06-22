r, c = map(int, input().split())
a, b = '.'*(c-1), '#'
for i in range(r):
    print((a+b if i % 4 < 2 else b+a)if i % 2 else b*c)
