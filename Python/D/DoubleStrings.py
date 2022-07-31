for cases in range(int(input())):
    n = int(input())
    a = [input() for i in range(n)]
    s = set(a)
    for i in a:
        flag = 0
        for j in range(1, len(i)):
            if i[:j] in s and i[j:] in s:
                flag = 1
                break
        print(flag, end='')
    print()
