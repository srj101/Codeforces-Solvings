n = input()
n = 0
x = list(map(int, input().split()))
x.reverse()
for i in x:
    n = min(0, n+i)
print(-n)
