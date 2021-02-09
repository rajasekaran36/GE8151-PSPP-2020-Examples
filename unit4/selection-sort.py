numbers = [6,7,3,1,5,2,4]
print('before sorting:',numbers)

for i in range(len(numbers)-1):
    #minimum = min(numbers[i:])
    #minimum_index = numbers.index(minimum)
    
    minimum_index = i
    for j in range(i+1,len(numbers)):
        if(numbers[j]<numbers[minimum_index]):
            minimum_index = j
    
    if(i!=minimum_index):
        numbers[i],numbers[minimum_index]=numbers[minimum_index],numbers[i]
    print(numbers)

print('after sorting',numbers)
 