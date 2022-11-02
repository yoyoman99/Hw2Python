def swap_list(list):
    midIndex = (len(list)-1)//2
    lastIndex = len(list) - 1
    list[midIndex],list[lastIndex] = list[lastIndex],list[midIndex]
    return list
list1 = [1,"hi",3,"yo",6]
print(swap_list(list1))