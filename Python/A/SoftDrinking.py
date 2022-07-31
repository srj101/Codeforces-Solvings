n, k, l, c, d, p, nl, np = map(int, input().split())
total = k*l
drinks = total//nl  # toasts
limes = c*d         # toasts
salts = p//np       # toasts
canMake = min(drinks, limes, salts)//n  # toasts
print(canMake)
