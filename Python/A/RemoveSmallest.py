t = int(input())
while t > 0:
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    remover = []
    for i in range(0, len(nums)-1):
        if abs(nums[i]-nums[i+1]) < 2:
            remover.append(nums[i])
    for j in remover:
        nums.remove(j)
    print("YES") if len(nums) < 2 else print("NO")
    t -= 1
