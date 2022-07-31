for cases in range(int(input())):
    a = list(map(int, input().split()))
    t1 = max(a[0], a[1])
    t2 = max(a[2], a[3])
    a = sorted(a, reverse=True)
    m1 = a[0]
    m2 = a[1]
    test = [m1, m2]
    if t1 in test and t2 in test:
        print("YES")
    else:
        print("NO")
