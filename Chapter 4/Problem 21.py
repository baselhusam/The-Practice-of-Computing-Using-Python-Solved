#Exercise 21

inp = input("Enter a string: ")

all_characters = "qwertyuiopasdfghjklzxcvbnm1234567890 " #all character and numbers and space
output = ""

for i in inp:
    if i.lower() in all_characters:
        output += i #concatenating 
        
print(output)
        
    