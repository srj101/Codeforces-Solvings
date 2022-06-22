g = 0
s = ""
for i in range(int(input())):
    l = input()
    if(l != s):
        s = l
        g += 1
print(g)
