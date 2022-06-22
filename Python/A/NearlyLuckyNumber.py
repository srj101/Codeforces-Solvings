number = list(input())
count = 0
for n in number:
    if n == "7" or n == "4":
        count += 1
if count == 7 or count == 4:
    print("YES")
else:
    print("NO")
