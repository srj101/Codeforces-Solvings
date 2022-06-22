n = int(input())
for cases in range(0, n):
    s = input()
    e = list(map(int, input().split()))
    o = 0
    ev = 0
    for i in e:
        if i % 2 == 0:
            ev += 1
        else:
            o += 1
    print(min(o, ev))
