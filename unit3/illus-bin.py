def bin_search(numbers,key):
    len_of_numbers = len(numbers)
    if(len_of_numbers==0):
        return 'empty'
    elif(len_of_numbers==1):
        if(key==numbers[0]):
            return 0
        else:
            return 'not found'
    else:
        low = 0
        high = len_of_numbers-1
        while(not (low>high)):
            mid = (low+high)//2
            if(key == numbers[mid]):
                return mid
            else:
                if(key<numbers[mid]):
                    high = mid-1
                else:
                    low = mid+1
        else:
            return 'not found'

print('binary search')
#numbers = []
#numbers = [2]
numbers = [2,3,7,7,8,10,13,44,66]
key = int(input('enter key to be searched:'))
print(numbers)
print(bin_search(numbers,key))
            
        
