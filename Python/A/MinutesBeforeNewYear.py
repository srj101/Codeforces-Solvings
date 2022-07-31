for cases in range(int(input())):
    a, b = map(int, input().split())
    ans = 1440 - (a*60 + b)
    print(ans)
