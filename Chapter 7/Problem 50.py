#Exercise 50

inp = input("Enter whatever you want: ")
lst = []

while inp != "-1":
    lst.append(inp)
    inp = input("Enter -1 to exit the program: ")
    
print(lst)