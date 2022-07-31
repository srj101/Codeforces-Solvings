n = input()
a = list(map(int, input().split()))
mi = 0
if a.count(1) > 0 and a.count(2) > 0 and a.count(3) > 0:
    mi = min(a.count(1), a.count(2), a.count(3))
    print(mi)
    for i in range(mi):
        for j in range(1, 4):
            print(a.index(j)+1, end=' ')
            a[a.index(j)] = 0
        print()

else:
    print(mi)
