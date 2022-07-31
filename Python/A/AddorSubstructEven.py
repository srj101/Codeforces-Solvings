for cases in range(int(input())):
    a, b = map(int, input().split())

    if a == b:
        print('0')
    elif a < b:
        print(2-(b-a) % 2)
    else:
        print(1+(a-b) % 2)
