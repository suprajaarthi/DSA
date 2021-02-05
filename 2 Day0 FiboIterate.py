


def fib(n):
    if n == 0 or n == 1: return n
        # iterative solution
    a, b, c = 0, 1, 0
    while n > 1:
        n -= 1
        c = a + b
        a, b = b, c
	
    return c
    
print(fib(5))