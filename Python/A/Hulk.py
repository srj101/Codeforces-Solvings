n = int(input())
s = ["love", "hate"]
prev = "I "
front = " that"
lastfront = "it"
f = []
state = False
while n > 0:
    state = not(state)
    f.append(prev+s[state]+front)
    n -= 1
f[n-1] = f[n-1].replace("that", "it")
print(" ".join(f))
