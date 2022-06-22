n = int(input())
p = list(map(int, input().split()))
gift_from = []
for i in range(1, n+1):
    gift_from.append(str(p.index(i)+1))
print(' '.join(gift_from))
