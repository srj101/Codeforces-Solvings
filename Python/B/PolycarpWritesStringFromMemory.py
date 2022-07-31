for cases in range(int(input())):
    s = input()
    memory = []
    n = 1
    for i in range(len(s)):
        if s[i] not in memory:
            if len(memory) == 3:
                n += 1
                memory = [s[i]]
            else:
                memory.append(s[i])
    print(n)
