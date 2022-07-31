for cases in range(int(input())):
    n = input()

    a = list(map(int, input().split()))

    i = 0
    while len(a) > 0:
        print(a[0], end=" ")
        a = list(filter(lambda k: k != a[0], a))
    print("")
