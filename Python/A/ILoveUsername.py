n = int(input())
points = list(map(int, input().split()))

a = points[0]
b = points[0]
z = 0
u = 0

for i in points:
    if i > a:
        a = i
        z += 1
    if i < b:
        b = i
        u += 1
f = z+u
print(f)
