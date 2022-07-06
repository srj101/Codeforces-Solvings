def checkPalindrom(s):
    if s == s[::-1]:
        return True
    return False
 
for cases in range(int(input())):
    sz = int(input())
    s = list(input())
    middleChar = s[sz//2]
    ans = 1
    for i in range(sz//2+1, sz):
        if s[i] == middleChar:
            ans += 1
        else:
            break
    if sz&1:
        print(2*ans-1)
    else:
        print(2*ans)