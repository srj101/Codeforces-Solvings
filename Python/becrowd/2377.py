l,d=map(int,input().split())
k,p=map(int,input().split())
qtde_pedagios=int(l/d)
total=(k*l)+(p*qtde_pedagios)
print(total)