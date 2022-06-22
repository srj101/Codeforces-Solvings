# Checking weather all the elements are equal
def checkAllEqual(lst):
    res = all(ele == lst[0] for ele in lst)
    if(res):
        return True
    return False

# Check the list all evens ..


def IsListEven(my_list):
    allEven = True
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            allEven = False
    return allEven

# Sob Odd kina


def IsListOdd(my_list):
    allOdd = True
    for i in range(len(my_list)):
        if my_list[i] % 2 != 1:
            allOdd = False
    return allOdd


for cases in range(int(input())):
    size = int(input())
    inputArray = list(map(int, input().split(' ')))
    ok = 0
    if checkAllEqual(inputArray) == True:
        print("YES")
        ok = 1
    else:
        prevArray = inputArray
        for i in range(0, len(inputArray)):
            if i % 2:
                inputArray[i] += 1
        if IsListEven(inputArray) == True or IsListOdd(inputArray) == True:
            print("YES")
            ok = 1
        else:
            for i in range(0, len(prevArray)):
                if i % 2 == 0:
                    prevArray[i] += 1
            if IsListEven(prevArray) == True or IsListOdd(prevArray) == True:
                print("YES")
                ok = 1

    if ok == 0:
        print("NO")
