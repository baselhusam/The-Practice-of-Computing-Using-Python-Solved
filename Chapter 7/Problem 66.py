#Exercise 66

import string

vowel = "aoieu"
all_letters = string.ascii_letters #All letters

def translate(string):
    output = ""
    for i in string:
        if i in vowel:
            output += i
        elif i in all_letters:
            output += i + "o" + i
        else: #The space or any special character
            output += i 
    return output

inp = "this is fun" #This could be as input
print(translate(inp))
