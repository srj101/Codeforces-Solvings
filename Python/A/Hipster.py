blue, red = map(int, input().split())
cntD = 0
cntRest = 0
while min(blue, red) > 0:
    blue -= 1
    red -= 1
    cntD += 1
m = max(blue, red)
while m > 1:
    m -= 2
    cntRest += 1
print(cntD, cntRest)
