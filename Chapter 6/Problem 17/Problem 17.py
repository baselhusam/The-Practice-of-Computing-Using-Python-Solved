#Exercise 17

numbers = input("Enter the number of lines you want to delete: ").split()

file = open("test_file.txt","r")
output_file = open("new_text_file.txt","w")
line_counter = 0

for line in file:
    if str(line_counter) in numbers:
        line_counter+= 1
        continue
    else:    
        print(line, file=output_file)
        line_counter+= 1
        
file.close()
output_file.close()

    
