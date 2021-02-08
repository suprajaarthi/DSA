
number=123456789
n=len(str(number));i=0;k=n
while number>0 and i<=k:
    a=(number // 10**n % 10)
    i+=1
    print(a)
    n-=1

