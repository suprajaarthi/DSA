def factorial(n):    
    if n == 1:
        return 1    
    else:
        return n * factorial(n-1)
        # 5*factorial(4)
        # 5*4*factorial(3)
        # 5*4*3*factorial(2)
        # 5*4*3*2*factorial(1)
        # 5*4*3*2*1



n=5
print(factorial(n))