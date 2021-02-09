a = (1,2)
b = (1,2)
equal = True
for i in range(len(a)):
    if(a[i]==b[i]):
        continue
    else:
        equal=False
        break

if(a==b):
    print("both are equal")
else:
    print('not equal')

