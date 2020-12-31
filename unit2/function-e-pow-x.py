def factorial(n):
    if(n==0):
        return 1
    result = n
    while(n!=1):
        result = result * (n-1)
        n = n-1
    return result

def power(n,p):
    return n**p

def term(x,n):
    result = power(x,n)/factorial(n)
    return result

def epow(x,max):
    n = 1
    result = 1
    while(n<=max):
        result = result + term(x,n)
        n = n + 1
    return result

print(epow(1,10))
print(factorial(0))