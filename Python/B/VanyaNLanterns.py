n,m=(map(int,input().split()))
a=sorted(list(map(int,input().split())))
d=max(a[0],m-a[n-1])
for i in range(1,n):
    d=max(d,(a[i]-a[i-1])/2)
print(d)