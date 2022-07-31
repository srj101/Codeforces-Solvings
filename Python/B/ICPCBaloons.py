for cases in range(int(input())):
    n = input()
    s = list(input())
    k = set(s)
    point = len(k)*2
    for i in k:
        s.remove(i)
    extraPoint = len(s)
    point = point + extraPoint
    print(point)
