x,y = list(map(int, input().split()))
scores = list(map(int, input().split()))
count = 0
goal = scores[y-1]
for score in scores:
    if score > 0 and score>=goal:
        count+=1
print(count)