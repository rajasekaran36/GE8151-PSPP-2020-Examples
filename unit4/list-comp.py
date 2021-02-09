'''
def listCreator(end,start=1):
    alist = []
    for i in range(start,end+1):
        if(i%2!=0):
            alist.append(i)
    return alist

x = listCreator(1,100)
y = listCreator(1000,500)
z = listCreator(4000,5000)
h = listCreator(250)

alist = []
for i in range(10):
    alist.append(i)
'''
xlist = [1,2,3,3,4,5,2,2,4]
ylist = [5,4]
alist = [element for element in xlist if(element in ylist)]

print(alist)