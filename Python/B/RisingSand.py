for cases in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    for i in range(1,len(a)-1):
        if a[i] > a[i-1]+a[i+1]:
            c+=1
    print(((n-1)//2)) if k==1 else print(c)