n = input()
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += max(a) - i
print(abs(ans))
