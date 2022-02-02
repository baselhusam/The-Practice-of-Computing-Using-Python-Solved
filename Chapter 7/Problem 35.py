#Exercise 35

def rev(string):
    new_string = ""
    for i in reversed(string):
        new_string += i
    return new_string

inp = "stressed" #This string could be as input
print(rev(inp))