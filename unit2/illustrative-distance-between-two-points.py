import mymath
x1 = int(input("Enter x1"))
y1 = int(input("Enter y1"))
x2 = int(input("Enter x2"))
y2 = int(input("Enter y2"))

print("Point 1: ",(x1,y1))
print("Point 2:",(x2,y2))

result = mymath.sq_root(mymath.square(x2-x1)+mymath.square(y2-y1))
print("Distance between ",(x1,y1),"and",(x2,y2),"is:",result)