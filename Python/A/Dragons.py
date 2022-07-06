s,n = map(int,input().split())
z = []
for i in range(n):
    x,y = map(int,input().split())
    z.append((x,y))
z.sort()
flag = True
for j in z:
    if s > j[0]:
        s+=j[1]
    else:
        flag = False
        break
print("NO") if flag==False else print("YES")