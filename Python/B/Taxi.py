n = input()
groups = map(int, input().split())
putkey = [0]*5
for x in groups:
    putkey[x] += 1
ress = putkey[3]+putkey[4]
putkey[1] = max(putkey[1]-putkey[3], 0)
ress += (putkey[2]*2+putkey[1]+3)/4
print(int(ress))
