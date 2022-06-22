t = int(input())
while t > 0:
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        # Math.abs(Math.floor(0-Math.abs((1337-420))/10))
        # Formula
        # why ceil is not working in online compiler!!?
        print(abs(0--abs(a-b)//10))
    t -= 1
