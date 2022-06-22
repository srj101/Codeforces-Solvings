l,b = list(map(int,input().split()))
y=0
while l<=b:
    l = l*3
    b = b*2
    y+=1
print(y)