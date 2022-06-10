n = int(input())
x=0
while n>0:
    stmt = input()
    if stmt == "X++" or stmt == "++X":
        x+=1
    if stmt == "X--" or stmt == "--X":
        x-=1
    n-=1
print(x)