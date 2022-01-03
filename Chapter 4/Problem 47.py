#Exercise 47

password = input("Please enter your password here: ")

def fullcheck(password): #function will check all conditions for the valid password
    if checklen(password) and checkletter(password):
        return valid()
    else:
        return invalid()


def valid(): #function the print a statement if the password is valid
    print("Done, the password is valid.")
    
def invalid():#function the print a statement if the password is NOT valid
    print("Ops, the password is NOT valid.")



def checklen(password): #function will check the length for the password if it is between 6 and 20
    ln = len(password)
    if ln >= 6 and ln <= 20:
        return True
    else:
        return False
    
        
def checkletter(password): #function will check if the password has upper, lower, and numbers in it.

    upper, lower, num = 0,0, False #to count the lower and upper charecters in the string and the number of numbers
    numbers = [str(i) for i in range(0,10)] #make a list for any possible number and convert it to string, because the input will come as a string
    
    for i in password:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i in numbers:
            num = True
        if lower >= 1 and upper >= 1 and num: #this condition to break the for loop if all conditions became True
            return True
    return False #if not all condition came true then will return False
        

fullcheck(password)