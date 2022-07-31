mP = 0
cP = 0
for cases in range(int(input())):
    m, c = map(int, input().split())
    if m > c:
        mP += 1
    elif m == c:
        continue
    else:
        cP += 1
if mP > cP:
    print("Mishka")
elif mP == cP:
    print("Friendship is magic!^^")
else:
    print("Chris")
