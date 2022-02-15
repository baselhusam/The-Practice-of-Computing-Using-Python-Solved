#Exercise 7

# just examples
# my_dict = {'a':1, 'b':2,'c':3}
# your_dict = {'c':4,'d':5,'e':6}

#A)
def merge_dicts(dict1,dict2):
    return dict1 | dict2

# print(merge_dicts(my_dict, your_dict))

#B) 
def add_dicts(dict1,dict2):
    dict1.update(dict2)
    return dict1

# print(add_dicts(my_dict, your_dict))