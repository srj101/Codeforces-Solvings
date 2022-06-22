for cases in range(int(input())):
    n = int(input())
    if n % 4 == 0:
        print("YES")
        a = list(range(2, n + 1, 2))
        s = sum(a)
        for i in range(1, n - 1, 2):
            a.append(i)
            s -= i
        a.append(s)
        print(" ".join(map(str, a)))
    else:
        print("NO")
