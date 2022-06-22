n1 = list(input())
n2 = list(input())
ans = []
for i in range(0, len(n1)):
    if (int(n1[i]) + int(n2[i])) == 2:
        ans.append("0")
    else:
        ans.append(str(int(n1[i]) + int(n2[i])))
print("".join(ans))
