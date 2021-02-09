a = [1,3,4]
key = 7
ipos = 1
print('before insert:',a)
'''
for i in range(len(a)):
    if(i==ipos):
        temp = a[i]
        a[i] = key
    else:
        a[i] = a[i+1]
'''
a = a[0:ipos]+[key]+a[ipos:]
print('after insert:',a)