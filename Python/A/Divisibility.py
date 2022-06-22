import sys
input = sys.stdin.readline
for t in range(0, int(input())):
    count = 0
    a, b = map(int, input().split())
    print((b-a % b) % b)
