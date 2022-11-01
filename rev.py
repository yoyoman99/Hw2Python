def reverse_list(list1):
    if isinstance(list1, list):
        temp = [] 
        for e in reversed(list1):
            temp.append(e)
        return temp
    else:
        print("Invalid Input")
        return
