def unique_finder(a_list):
    unique = []
    for element in a_list:
        if(a_list.count(element)==1):
            unique.append(element)
    return unique
a_list = [2,4,5,1,6,1,3,5,6,8,10,1]
x_list = [3,5,2,3,1]

print(unique_finder(a_list))
print(unique_finder(x_list))

