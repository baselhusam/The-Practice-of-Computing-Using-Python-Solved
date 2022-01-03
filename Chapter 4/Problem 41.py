#Exercise 41

from prettytable import PrettyTable

table = PrettyTable()

table.title = "Melting and Boiling Points of Alkanes"
table.field_names = ['Name','Melting Point (deg C)',"Boiling Point (deg C)"]
table.add_row(["Methane" , -162 , -183])
table.add_row(["Ethane" , -89 , -172])
table.add_row(["Propane" , -42 , -188])
table.add_row(["Butane" , -0.5 , -135])

print(table)

