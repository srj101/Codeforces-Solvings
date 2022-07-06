for cases in range(int(input())):
    sz = input()
    a = list(map(int,input().split()))
    print(max(a)-min(a))