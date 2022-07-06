n = int(input())
a = list(map(int,input().split()))
pointsTable = [0,0]
k = 0
while len(a)>0:
    pointsTable[k%2] += max(a[0],a[-1])
    a.remove(max(a[0],a[-1]))
    k+=1
 
print(pointsTable[0],pointsTable[1])