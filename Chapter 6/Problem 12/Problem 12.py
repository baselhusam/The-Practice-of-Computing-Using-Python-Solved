#Exercise 12

def sort_file(file_name):
    try:
        file = open(file_name,"r")
        words = [word.lower() for line in file for word in line.split()] #Read every word in the file then change it to lower
        words.sort() #Sort the words in the list alphabetically
        return " ".join(words)
    
    except FileNotFoundError :
        print("Your file is not found, try again and be specific with the name and the path")
        new_file_name = input("Enter file name: ")
        print(sort_file(new_file_name))
        
        
file_name = input("Enter file name: ")
print(sort_file(file_name))

 