# Exercise 16



while True: #for iterating if the the input was wrong
    try: 
        file_name = input("Enter the file name: ")
        file = open(file_name,"r")
        
        for line in file: #line by line
            out = ""
            for char in line: #char by char
                out = char + out #reversed concatenation for reversed line
            print(out) #print the reversed line
            
        break # if it happened then the file is exsist and finish the program by braek the while loop
    except FileNotFoundError:
        print("The File is not found\nPlease try again and be sure about the path and the extenstion for the file")

file.close()




