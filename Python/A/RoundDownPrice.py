rounds = []
for i in range(0, 10):
    rounds.append(pow(10, i))

for cases in range(int(input())):
    n = int(input())
    idx = 0

    for j, val in enumerate(rounds):
        if val > n:
            idx = j
            break
    ans = n - rounds[idx-1]
    print(ans)
