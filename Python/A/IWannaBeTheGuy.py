n = int(input())
p = input().split()[1:]
q = input().split()[1:]
# print(p)
# print(q)
set_pq = set(p+q)
# print(p+q)
# print(set_pq)
if len(set_pq) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
