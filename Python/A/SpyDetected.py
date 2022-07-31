for cases in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    s = list(set(a))
    s1 = a.count(s[0])
    s2 = a.count(s[1])

    idx = 0
    if s1 == 1:
        idx = a.index(s[0]) + 1
    else:
        idx = a.index(s[1]) + 1
    print(idx)
