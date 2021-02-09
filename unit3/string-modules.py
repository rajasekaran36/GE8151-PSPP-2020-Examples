import string

def countAnything(data,compare):
    count = 0
    for chr in data:
        if(chr in compare):
            count +=1
    return count

a_string = 'python is5 EAsy3 to 2learn'

print('letters count',countAnything(a_string,string.ascii_letters))
print('lower count',countAnything(a_string,string.ascii_lowercase))
print('upper count',countAnything(a_string,string.ascii_uppercase))
print('digits count',countAnything(a_string,string.digits))
print('t count',countAnything(a_string,'t'))
































'''
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)  # ' \t\n\r\x0b\x0c'
print(string.punctuation)


'''