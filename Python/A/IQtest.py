n = input()
numbers = list(map(int, input().split()))
o = 0
e = 0
for i in numbers:
    if i % 2 == 0:
        o += 1
    else:
        e += 1
if o > e:
    for j in numbers:
        if j % 2 != 0:
            print(numbers.index(j)+1)
else:
    for k in numbers:
        if k % 2 == 0:
            print(numbers.index(k)+1)
