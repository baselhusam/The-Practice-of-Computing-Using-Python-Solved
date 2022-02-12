#Exercise 8 

def merge_lists(lst1,lst2):
    lst3 = lst1+lst2
    return list(set(lst3))

# an example:
# one = [1,2,3,4,5]
# two = [3,4,5,6,7]

# print(merge_lists(one, two))