from itertools import accumulate as acc
import sys
input = sys.stdin.readline

s, cases = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
p = [0] + arr
for v in range(s):
    p[v+1] += p[v]
for case in range(cases):
    x, y = map(int, input().split())
    print(p[x] - p[x-y])
