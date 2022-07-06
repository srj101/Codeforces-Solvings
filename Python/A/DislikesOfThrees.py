a = [0]
for i in range(1,1667):
    if i%3 != 0 and i%10 !=3:
        a.append(i)
for cases in range(int(input())):
    n = int(input())
    print(a[n])
