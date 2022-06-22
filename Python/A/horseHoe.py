def doStuff(n):
    return n


cloths = list(map(doStuff, input().split()))
c = set()
g = []
for cloth in cloths:
    c.add(cloth)

for i in c:
    g.append(cloths.count(i)-1)
print(sum(g))
