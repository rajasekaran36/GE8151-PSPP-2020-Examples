print('binary search')
numbers = [2,3,7,8,10,13,44,66]
key = int(input('enter key to be searched:'))
low = 0
high = len(numbers)-1
while(not (low>high)):
    mid = (low+high)//2
    if(numbers[mid]==key):
        print('element',key,'found at',mid,)
        break
    else:
        if(key<numbers[mid]):
            high=mid-1
        else:
            low=mid+1
else:
    print('element not found')
