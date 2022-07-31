for cases in range(int(input())):
    n = int(input())
    for i in range(1, n-2, 2):
        print(i+1, i, end=" ")
    if n % 2 == 0:
        print(n, n-1, end=" ")
    else:
        print(n, n-2, n-1, end=" ")
    print("")
