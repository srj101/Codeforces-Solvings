for cases in range(int(input())):
    n = int(input())
    o = n//3
    t = (n//3)
    r = n - (n//3 + (n//3)*2)
    if r == 0:
        print(o, o)
    elif r > 1:
        t += 1
        print(o, t)
    else:
        o += r
        print(o, t)
