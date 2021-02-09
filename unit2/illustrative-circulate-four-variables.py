# circulate the values of n variables
a=10
b=20
c=30
d=40
# first
print("Before Circulate")
print("a=",a,"b=",b,"c=",c,"d=",d)

temp = a
a = b
b = c
c = d
d = temp


# second
print("After Circulate")
print("a=",a,"b=",b,"c=",c,"d=",d)
temp = a
a = b
b = c
c = d
d = temp

print("After Circulate 2")
print("a=",a,"b=",b,"c=",c,"d=",d)
