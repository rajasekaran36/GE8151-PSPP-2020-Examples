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

def square(n):
    return n**2

def sq_root(n):
    return n**0.5
