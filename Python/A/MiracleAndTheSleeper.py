for cases in range(int(input())):
    x, y = map(int, input().split())
    if x > y//2:
        print(y-x)
    else:
        print((y-1)//2)
