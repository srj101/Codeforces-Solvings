sx = sorted(list(map(int, input().split())), reverse=True)
a = max(sx) - min(sx)
sx.remove(max(sx))
sx.remove(min(sx))
c = sx[0] - a
b1 = min(sx) - c
b2 = sx[1] - a
print(abs(a), abs(min(b1, b2)), abs(c))
