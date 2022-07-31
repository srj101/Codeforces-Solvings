for cases in range(int(input())):
    a, b, c = map(int, input().split())
    A = max(a, b+1, c+1)-a
    B = max(a+1, b, c+1)-b
    C = max(a+1, b+1, c)-c
    print(A, B, C)
