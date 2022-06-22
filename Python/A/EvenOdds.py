n, k = map(int, input().split())
middle = (n+1)//2
if k <= middle:
    print(k*2-1)
else:
    print((k-middle)*2)
