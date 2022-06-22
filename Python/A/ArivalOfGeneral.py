n = int(input())
slds = list(map(int, input().split()))
ans = slds.index(max(slds)) + slds[::-1].index(min(slds))
if ans >= n:
    print(ans-1)
else:
    print(ans)
