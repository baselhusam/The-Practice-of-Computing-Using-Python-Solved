#Exercise 9

def solve(string):
    dig = tuple([i for i in string if i.isdigit()])
    letters = [i for i in string if i.isalpha()]
    return [dig, letters]


    