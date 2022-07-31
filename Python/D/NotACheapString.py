for cases in range(int(input())):
    n = input()
    k = int(input())
    arr = []
    price = 0
    for i, char in enumerate(n):
        arr.append((ord(char)-96, i))
        price += ord(char)-96
    sorted_arr = sorted(arr)
    while price > k:
        nu, i = sorted_arr.pop(-1)
        price -= nu
        arr[i] = 0
    print("".join([n[i] for i in range(len(n)) if arr[i]]))
