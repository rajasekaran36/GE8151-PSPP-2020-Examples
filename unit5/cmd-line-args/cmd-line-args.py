import sys
def invert_dict(a_dict):
    in_dict = {}
    for key in a_dict:
        in_dict[a_dict[key]] = key
    return in_dict

def bar_chart(a_dict):
    keys = list(a_dict.keys())
    print(keys)
    #keys.sort()
    for key in keys:
        print(a_dict[key],"\t\t:"+'#'*key)
    
args = sys.argv
file = open(args[1],'r')
data = file.read()
data = data.lower()
datas = data.split(' ')
alist = [data.replace('\n','') for data in datas if data.isalpha()]
print(alist)
histo = {}
for element in alist:
    if(histo.get(element)):
        histo[element] = histo[element] + 1
    else:
        histo[element] = 1

#unique words
# for key in histo:
#     if(histo[key] == 1):
#         print(key)

#max 
max = 0
max_word = ''
for key in histo:
    if(histo[key]>max):
        max = histo[key]
        max_word = key

print(max_word,'---',max)
file.close()

bar_chart(invert_dict(histo))
