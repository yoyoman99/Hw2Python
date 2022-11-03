def sort_dictionary(dict):
    list1 = []
    i = 1
    for i in range(0,len(dict)):
        min_age = list(dict.values())[0][1]
        min_person = list(dict.keys())[0]
        for j in dict:
            current = dict[j][1]
            if min_age >= current:
                min_age = current
                min_person = j
        phone_number = dict[min_person][0]
        tuple = (min_person,phone_number)
        list1.append(tuple)
        del dict[min_person] 

    return list1           