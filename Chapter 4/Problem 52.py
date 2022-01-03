#Exercise 52

orderd_numbers = "123456789"
solve = False

while not solve:
    inp = input("Enter three-digit number: ")
    
    if len(inp) == 3 :
        if inp in orderd_numbers:
            solve = True
            print("CORRECT INPUT, GOOD JOB.")
        else:
            print("Error: the input are not in order.\ntry again")
    else:
        print("Error: The input is more than 3 digits.\ntry again")