from datetime import datetime
import datetime

def list_printer(list_data):
    for data in list_data:
        print(data)
chat_file = open('chat-file.txt','r')
chat_data = chat_file.readlines()

chat_data = [data for data in chat_data if(data!='\n')]
chat_data = [data.replace('\n','') for data in chat_data]
print(len(chat_data))
message_data = []
for i in range(0,len(chat_data),2):
    message_data.append(chat_data[i])

chat_dict = {}

for message in message_data:
    s_message = message.split(':')
    if(len(s_message)==2):
        chat_dict[s_message[0]] = s_message[1]

present = []
for key in chat_dict:
    message = chat_dict[key]
    message = message.lower()
    if(message.find('present')!=-1):
        present.append(key)

present.sort()
print(str(datetime.now()))
file_to_write = open('present.txt','w')
file_to_write.write(str(datetime.now())+'\n\n\n')
for student in present:
    file_to_write.write(student+'\n')
file_to_write.close()

#print(chat_data)
#list_printer(message_data)
chat_file.close()