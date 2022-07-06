n = int(input())
h = []
g = []
for i in range(n):
    x,y = map(int,input().split())
    h.append(x)
    g.append(y)
c = 0
for i in g:
    c+=h.count(i)
print(c)