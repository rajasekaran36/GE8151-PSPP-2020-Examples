numbers = [6,7,3,1,5,2,4]

for i in range(1,len(numbers)):
    key = numbers[i]
    j = i - 1
    while(j>=0 and key<numbers[j]):
        numbers[j+1] = numbers[j]
        j=j-1
    numbers[j+1]=key

print(numbers)