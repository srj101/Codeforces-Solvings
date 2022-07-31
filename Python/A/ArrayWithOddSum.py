for cases in range(int(input())):
    k = input()
    a = [int(i) % 2 for i in input().split()]
    if sum(a) % 2 == 1:
        print("YES")
    elif len(set(a)) == 1:
        print("NO")
    else:
        print("YES")
