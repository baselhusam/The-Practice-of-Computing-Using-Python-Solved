#Exercise 18

inp = input("Enter string here: ")
lower, upper =0,0

for i in inp:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
        
print("Number of uppercase letters is: {} \nNumber of lowercase letters is: {}".format(upper,lower))
