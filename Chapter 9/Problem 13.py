#Exercise 13

d = {"basel":19, "husam":53}

name = input("Enter name of the person: ")

if name in d.keys():
    print(d[name])
else:
    age = int(input("name is not found, enter his age: "))
    d[name] = age
    
    