n, t = map(int, input().split())
at = (4*60 - t)
while ((n*(n+1))//2)*5 > at:
    n -= 1
print(n)
