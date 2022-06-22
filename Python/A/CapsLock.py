s = input()
st = s[1:]
if s == s.upper():
    print(s.lower())
elif st == st.upper():
    print(s.capitalize())
else:
    print(s)
