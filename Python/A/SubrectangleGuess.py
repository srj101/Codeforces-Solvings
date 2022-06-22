negative_infnity = float('-inf')
positive_infinity = float('inf')

for cases in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    maximum = negative_infnity
    ans = positive_infinity
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            maximum = max(maximum, val)

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == maximum:
                c1 = (i+1)*(j+1)
                c2 = (n-i)*(j+1)
                c3 = (n-i)*(m-j)
                c4 = (i+1)*(m-j)
                c1 = max(c1, max(c2, max(c3, c4)))
                ans = min(ans, c1)
    print(ans)
