#Exercise 49

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = [ i for i in range(1,11)] #number from 1 to 10 as column name

for j in range(13):
    row = [j*i for i in range(1,11)] #multiplicate every number form 0 to 12 of numbers from 1 to 10
    table.add_row(row) # added the list as a row
    
print(table)
    