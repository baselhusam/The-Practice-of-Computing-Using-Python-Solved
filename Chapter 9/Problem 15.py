#Exercise 15

#A)
def solve_a():
    first, last = input("Enter your \" firstNmae lastName \": ").split()
    f_list = list(first)
    l_list = list(last)
    return [i for i in f_list if i in l_list]

#B)
def solve_b():
    first, last = input("Enter your \" firstNmae lastName \": ").split()
    f_set = set(list(first))
    l_set = set(list(last))
    return f_set.intersection(l_set)

#C)
def solve_c():
    first, last = input("Enter your \" firstNmae lastName \": ").split()
    f_set = set(list(first))
    l_set = set(list(last))
    return f_set.symmetric_difference(l_set)
