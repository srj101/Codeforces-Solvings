import re
string = input()
print("YES"if re.search("h.*e.*l.*l.*o", string) else"NO")
