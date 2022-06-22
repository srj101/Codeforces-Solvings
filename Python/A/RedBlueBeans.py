for cases in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if abs(a-b) <= min(a, b)*c else "NO")
