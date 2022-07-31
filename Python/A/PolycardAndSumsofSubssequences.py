for cases in range(int(input())):
    a = list(map(int, input().split()))
    f = a[0]
    s = a[1]
    l = a[6] - f - s
    print(f, s, l)
