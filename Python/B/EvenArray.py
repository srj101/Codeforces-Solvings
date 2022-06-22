for testcases in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    e = 0
    o = 0
    for i in range(n):
        if i % 2 == 0:
            if l[i] % 2 == 0:
                e += 1
            else:
                c += 1
                o += 1
        else:
            if l[i] % 2 == 0:
                c += 1
                e += 1
            else:
                o += 1
    if c % 2 == 0 and (e == o or e == (o+1)):
        print(c//2)
    else:
        print("-1")
