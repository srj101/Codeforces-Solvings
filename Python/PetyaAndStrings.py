string1 = input()
string2 = input()
if string1.upper() == string2.upper():
    print(0)
elif string1.upper() < string2.upper():
    print(-1)
else:
    print(1)