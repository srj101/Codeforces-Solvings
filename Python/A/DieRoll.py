y, w = map(int, input().split())
p = ['', '1/1', '5/6', '2/3', '1/2', '1/3', '1/6']
mx = max(y, w)
print(p[mx])
