string1 = input()
string2 = list(input())
string2.reverse()
string2 = "".join(string2)
if string1 == string2:
    print("YES")
else:
    print("NO")
