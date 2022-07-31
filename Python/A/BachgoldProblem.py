n = int(input())
d = n
a = []
if n % 2 == 0:
    a = [2]*(n//2)
else:
    a = [2]*((n-3)//2)
    a.append(3)

print(len(a))
for k in a:
    print(k, end=' ')
