# Exercise 42

from tabulate import tabulate

inp = input("Enter string here: ")
digits, letters, specials = 0,0,0

for i in inp:
    if i.isnumeric():
        digits += 1
    elif i.isalpha():
        letters += 1
    elif not i.isspace():
        specials += 1
        

table = [['Digital Numbers', 'Letters', 'Special Characters'], [digits, letters, specials]]

print("\n\n",tabulate(table, headers = 'firstrow'))
