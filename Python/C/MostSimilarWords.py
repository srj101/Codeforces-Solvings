def dif(c):
    return abs(ord(c[1]) - ord(c[0]))


def costCalc(w1, w2):
    n = len(w1)
    cost = 0
    return sum(list(map(dif, list(zip(w1, w2)))))


t = int(input())
while t > 0:
    n, l = map(int, input().split())
    words = []
    while n > 0:
        words.append(input())
        n -= 1
    diffs = []
    for bg in range(0, len(words)):
        for dg in range(bg+1, len(words)):
            diffs.append(costCalc(words[dg], words[bg]))
    print(min(diffs))
    t -= 1
