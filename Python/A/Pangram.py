n = input()
s = input().lower()
al = list("abcdefghijklmnopqrstuvwxyz")
cnt = 0
for c in range(0, len(al)):
    if al[c] in s:
        cnt += 1
if cnt >= 26:
    print("YES")
else:
    print("NO")
