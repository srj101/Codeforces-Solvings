n = int(input())
coins = [100,20,10,5,1]
c = 0
for i in coins:
    if n>0 and n>=i:
        c+=n//i
        n-= i*(n//i)
print(c)
