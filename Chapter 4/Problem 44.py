#Exercise 44

from prettytable import PrettyTable

inp = input("Enter a string here: ")
digits, upper, lower, specials = 0,0,0,0

for i in inp:
    if i.isnumeric():
        digits += 1
    elif i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    elif not i.isspace():
        specials += 1


table = PrettyTable()

table.field_names = ['No. uppercase', 'No. lowercase', 'No. digital','No. punctuation']        
table.add_row([upper, lower, digits, specials])

print(table)