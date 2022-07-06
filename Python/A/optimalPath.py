for cases in range(int(input())):
    n,m=map(int, input().split())
    print(int(m*(m+1)/2+m*n*(n+1)/2-m))