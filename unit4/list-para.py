def printA(x):
    c = x[:]
    c[0] = c[0]+10
    print(c)

a = [10]
print(a)
printA(a)
print(a)