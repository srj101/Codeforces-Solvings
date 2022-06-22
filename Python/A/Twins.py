n = input()
coins = list(map(int, input().split()))
coins = sorted(coins, reverse=True)
myTotal = 0
count = 0
while (myTotal <= sum(coins)) and len(coins) > 0:
    myTotal += coins[0]
    count += 1
    coins.pop(0)
print(count)
