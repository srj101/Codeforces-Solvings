t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    print('NO') if w*h & -w*h < n else print('YES')
