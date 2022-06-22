import math


def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a+1
    return num > 1


n = int(input())
x = 1
a = n//2
b = n-a
while True:
    if (isprime(a) == False) and (isprime(b) == False):
        break
    a = n//2 - x
    b = n - a
    x += 1
print(a, b)
