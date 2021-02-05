def fibo(n):
	if n==0:
		return 0 

	elif n==1:
		return 1 

	else:
		return fib(n-1)+fib(n-2)


print(fib(5))
print(fib(6))


# while calling fib function instead of calculating each time call for prev numbers  
# fib(2)=fib(0)+fib(1)=1
#fib(3)=fib(2)+fib(1)=2 
# fib(4)=fib(3)+fib(2)=2+1=3
# 0, 1, 1, 2, 3, 5, 8, 13,