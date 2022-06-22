for cases in range(int(input())):
    size = int(input())
    inputArray1 = list(map(int, input().split()))
    inputArray2 = list(map(int, input().split()))
    sdjkgb = []
    for i in range(size):
        sdjkgb.append(min(inputArray1[i], inputArray2[i]))
    print(max(max(inputArray1), max(inputArray2))*max(sdjkgb))
