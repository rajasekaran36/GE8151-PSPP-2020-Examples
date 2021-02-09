print('linear search')
numbers = [2,3,7,8,10,13,44,66]
key = int(input('enter key to be searched:'))

for i in range(len(numbers)):
    #print(numbers[i])
    if(key == numbers[i]):
        print('element',key,'is found at index position ',i)
        break
else:
    print('element not found')
