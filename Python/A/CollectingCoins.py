for cases in range(int(input())):
    a, b, c, d = map(int, input().split())
    req = 0
    for i in [a, b, c]:
        req += max([a, b, c]) - i
    if req <= d and (d-req) % 3 == 0:
        print("YES")
    else:
        print("NO")
