def deepcopier(a):
    b = []
    for element in a:
        if(type(element) is list):
            b.append(element.copy())
        else:
            b.append(element)    
    return b

a = [1,2,[30,40,[60,70]]]
b = deepcopier(a)

print('a:',a)
print('b:',b)
a[2][2][0]=600
print('a:',a)
print('b:',b)