n, m = map(int,input().split())
houses = list(map(int,input().split()))
curr = 1
ans = 0
 
for i in houses:
    ans+=(i-curr)%n
    curr=i
    
print(ans)