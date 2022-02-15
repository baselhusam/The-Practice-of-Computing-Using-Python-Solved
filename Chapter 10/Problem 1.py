#Exercise 1

#A)
def sum_lists_a(list1,list2):
    sums_list = []
    for index in range(len(list1)):
        sums_list.append(list1[index] + list2[index])
    return sums_list

#B)
def sum_lists_b(list1,list2):
    sums_list = []
    if len(list1) > len(list2):
        for index in range(len(list2)):
            sums_list.append(list1[index] + list2[index])
        for index in range(len(list2),len(list1)):
            sums_list.append(list1[index])
    else:
        for index in range(len(list1)):
            sums_list.append(list1[index] + list2[index])
        for index in range(len(list1),len(list2)):
            sums_list.append(list1[index])
   
#C)
def sum_lists_c(list1,list2):
    return [list1[i] + list2[i] for i in range(len(list1))]
