n = int(input())
s = input()
d = s.count("D")
a = s.count("A")
if d == a:
    print("Friendship")
elif d > a:
    print("Danik")
else:
    print("Anton")
