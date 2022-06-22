n = int(input())
votes = list(map(int, input().split()))
flag = False
for vote in votes:
    if vote == 1:
        flag = True
        break
if flag == True:
    print("HARD")
else:
    print("EASY")
