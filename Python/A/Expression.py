n1 = int(input())
n2 = int(input())
n3 = int(input())
f1 = n1+n2*n3
f2 = n1*(n2+n3)
f3 = n1*n2*n3
f4 = (n1+n2)*n3
f5 = n1+n2+n3
a = [f1, f2, f3, f4, f5]
print(max(a))
