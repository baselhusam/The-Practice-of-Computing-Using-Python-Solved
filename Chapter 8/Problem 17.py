#Exericse 17

#A)
def remove_even(lst):
    return [i for i in lst if i%2 != 0]

#B)
def remove_odd(lst):
    return [i for i in lst if i%2 == 0]

#C)
def new_func(lst,boolean):
    if boolean:
        return remove_odd(lst)
    else:
        return remove_even(lst)