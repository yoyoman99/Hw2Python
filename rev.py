def reverse_list(list):
    temp = [] 
    for i in range(len(list)-1,-1,-1):
        temp.append(list[i])
    return temp
list1 = []
print(reverse_list(list1))