for cases in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    a1 = a[:n]
    a2 = sorted(a[n:])

    for i in range(0, n):
        if abs(a2[i] - a1[i]) >= x:
            a2[i] = 0

    print("YES") if a2.count(0) == n else print("NO")
