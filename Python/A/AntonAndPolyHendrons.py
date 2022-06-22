n = int(input())
ans = 0
for i in range(0, n):
    s = input()
    if s == "Icosahedron":
        ans += 20
    if s == "Cube":
        ans += 6
    if s == "Tetrahedron":
        ans += 4
    if s == "Dodecahedron":
        ans += 12
    if s == "Octahedron":
        ans += 8
print(ans)
