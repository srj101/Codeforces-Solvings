s = list(input())
i = 0
res = []
while i < len(s):
    if s[i] == "-" and s[i+1] == ".":
        res.append('1')
        i += 2
    elif s[i] == "-" and s[i+1] == "-":
        res.append('2')
        i += 2
    else:
        res.append('0')
        i += 1

print("".join(res))
