#Exercise 26

def rotate_string(string):
    return string[-1] + string[:-1]

inp = input("Enter a string here: ")
print(rotate_string(inp))