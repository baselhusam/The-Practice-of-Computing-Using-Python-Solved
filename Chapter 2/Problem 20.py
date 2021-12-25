#Exercise 20

inp = input("Input an integer: ")

while not inp.isdigit():
    inp = input("Error: try again. Input an integer: ")
    
print("The integer is:",inp)