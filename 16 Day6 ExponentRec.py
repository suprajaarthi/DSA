def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
		
# 		3*power(3,3)
# 		3*3*power(3,2)
#         3*3*3*power(3,1)
# if 1 return a
#         3*3*3*3*power(3,0)
# if 0 return 1
#         3*3*3*3*1
        
print(power(3,4))
