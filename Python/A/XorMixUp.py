from functools import reduce
 
def all_equal(List):
    return List.count(List[0]) == len(List)
     
 
for cases in range(int(input())):
    sz = input()
    a = list(map(int,input().split()))
    if len(a)==2 or all_equal(a):
        print(a[0])
    else:
        ans = a[0]
        i = 0
        for i in a:
            ne = n = [x for x in a if x != i]
            res = reduce(lambda i, j: int(i) ^ int(j), ne)
            if res==i:
                ans = i
                break
        print(ans)