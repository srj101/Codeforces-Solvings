import sys
input = sys.stdin.readline
for t in range(0, int(input())):
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if i > a[0]:
            c += 1
    print(c)
