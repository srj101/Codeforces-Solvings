a = list(map(int, input().split()))
b = list(map(int, input()))
p = 0
for i in b:
    if i == 1:
        p += a[0]
    elif i == 2:
        p += a[1]
    elif i == 3:
        p += a[2]
    else:
        p += a[3]
print(p)
