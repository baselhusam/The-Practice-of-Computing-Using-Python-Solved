#Exercise 6

#A)
file = open("thisFile.txt","w")

user_input= input("Write an input here to put it inside the file: ")

print(user_input, file = file)

file.close()