def circulateList(aList,n=1):
    pass
    # code

aList = []

no_of_elements = int(input("enter number of elements:"))
for i in range(no_of_elements):
    x = int(input())
    aList = aList + [x]

print("Before Circulate")
print(aList)
temp = aList[0]
for i in range(len(aList)-1):
    aList[i] = aList[i+1]
aList[len(aList)-1] = temp
print("After Circulate")
print(aList)


