n = int(input())
steps = [5, 4, 3, 2, 1]
count = 0
for step in steps:
    while n >= step:
        n -= step
        count += 1
print(count)
