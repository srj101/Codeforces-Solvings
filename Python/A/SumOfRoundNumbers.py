t = int(input())
g = [10, 100, 1000, 10000]
while t > 0:
    n = int(input())
    if len(str(n)) == 1:
        print(1)
        print(n)
    else:
        h = []
        for i in g:
            if ((n % i) - n % (i//10)) != 0:
                h.append((n % i) - n % (i//10))
        if len(h) == 0:
            print(1)
            print(n)
        else:
            print(len(h))
            for j in h:
                print(j, end=" ")
            print("\n")
    t -= 1
