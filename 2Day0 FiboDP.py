def fibo(n):
	fibarray=[0,1]
	for i in range(2,n+1):
		fibarray.append(fibarray[i-1]+fibarray[i-2])
	return fibarray[n]


print(fibarray[5])
print(fibarray[4])
print(fibarray)


5
fib.append(0,1,1,)
# 0
# 1 =1+0=1
# 2 =1+0=1
# 3 1+1=2
# 4  2+1=3
# 5 3+2=5

# [0, 1, 1, 2, 3, 5]
# array[5]=