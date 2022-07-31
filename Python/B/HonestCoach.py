def findMinDiff(arr, n):
    diff = 10**20
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(arr[i]-arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
    return diff


for cases in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = set(a)
    if len(s) != len(a):
        print("0")
    elif n == 2:
        print(a[1]-a[0])
    else:
        print(findMinDiff(a, n))
