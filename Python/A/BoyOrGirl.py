string = input()
s = set()
for i in list(string):
    s.add(i)
if len(s)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")