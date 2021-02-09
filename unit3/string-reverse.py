data = input('enter a string:')
rdata = data[::-1]
'''
palindrome = True
for i in range(len(data)):
    if(data[i]==rdata[i]):
        continue
    else:
        palindrome = False
        break
'''
if(data == rdata):
    print('it is a palindrome')
else:
    print('not a palindrome')
