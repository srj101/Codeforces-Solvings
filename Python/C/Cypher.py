for cases in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dic = []
    for i in range(n):
        s = input().split(" ")
        moveCount = int(s[0])
        moves = s[1]
        dic.append(moves)
    for i in range(0, n):
        for j in dic[i]:
            if j == "D":
                if a[i] == 9:
                    a[i] = 0
                else:
                    a[i] += 1
            else:
                if a[i] == 0:
                    a[i] = 9
                else:
                    a[i] -= 1
    for l in a:
        print(l, end=" ")
