n = int(input())
s = input()
cnt = 0
for i in range(n):
    if s[i:i+3] == 'xxx':
        cnt += 1
print(cnt)
