file_to_read = open('./file-read/file-read-source.txt','r')

print('FILE METHOD:read')
print('--------------------')
print(file_to_read.read())
print('--------------------')

# print('FILE METHOD:readline')
# print('--------------------')
# print(file_to_read.readline())
# print('--------------------')
# print('FILE METHOD:readlines')
# print('--------------------')
# print(file_to_read.readlines())
# print('--------------------')

file_to_read.close()