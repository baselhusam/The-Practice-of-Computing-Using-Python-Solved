#Exercise 7

import string

all_char = string.printable
all_num = string.digits
all_special_char = string.punctuation

all_things = [all_char, all_num, all_special_char]

file = open("jumble.txt","r")

space, tab, returns = 0,0,0

for line in file:
    for char in line:
        if char == "\n":
            returns += 1
        elif char not in all_things and not char.isspace():
            tab += 1
        elif char == " ":
            space += 1
            
            
print("No. spaces:",space)
print("No. tabs:", tab)
print("No. returns:",returns)