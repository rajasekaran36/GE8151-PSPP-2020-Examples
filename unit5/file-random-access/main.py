file = open('sun.jpg','rb')
data = file.read()
file.close()
file2 = open('copy_sun.jpg','wb')
file2.write(data)
file2.close()



# file.write('APPLE')
# file.seek(0)
# data = file.read()
# print(data)
# file.close()












# print('cur pos:',file.tell())
# file.seek(6)
# print('cur pos:',file.tell())
# data = file.read(6)
# print(data)
# print('cur pos:',file.tell())
















# file.write('\n'+'Orange')
# file.write('\n'+'Watermelon')
# file.close()
# print('cur pos:',file.tell())
# data = file.read()
# print(data)
# print('cur pos:',file.tell())
# file.seek(0)
# print('cur pos:',file.tell())
# data2 = file.read()
# print(data2)
# print('cur pos:',file.tell())
# file.close()