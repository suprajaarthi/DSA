def findgcd(a,b):
	low=min(a,b)
	high=max(a,b)
	if low==0:
		return high 
	if low==1:
		return low
	else:
		return findgcd(low,high%low)

		# 12,14 
		# 12,14%12
		# 12,2
		# l,h=2,12
		# 2,12%2
		# 2,0
		# l==0 ret high : 2 is the gcd of 12,14