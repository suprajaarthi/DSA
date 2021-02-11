
#  sum of n natural numbers 
def sumupton(n):
	if n==1:
		return 1 
	else:
		return  sumupton(n-1)+n
# sum(9)+10
# sum(8)+9+10
# sumu(7)+8+9+10


print(sumupton(10))
