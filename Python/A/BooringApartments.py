for cases in range(int(input())):
    n = int(input())
    cDict = {}
    for i in range(1,(n%10)+1):
        cDict[i] = [1,2,3,4]
    ans = 0
    for key,val in cDict.items():
        if key!=n%10:
            ans+=sum(val)
    ans += (len(str(n))*(len(str(n))+1))//2
    print(ans)