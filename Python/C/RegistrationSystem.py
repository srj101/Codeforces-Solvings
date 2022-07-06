d={}
for _ in range(int(input())):
	s=input()
	if s in d:
		print(s+str(d[s]))
		d[s]+=1
	else:
		d[s]=1
		print('OK')