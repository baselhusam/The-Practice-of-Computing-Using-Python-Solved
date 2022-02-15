#Exercise 26

num_words = {1:"one", 2:"two", 3:"three",
             4:"four", 5:"five", 6:"six",
             7:"seven", 8:"eight", 9:"nine",
             0:"zero"}

num = input("Enter number here: ")
out = ""

for i in num:
    out += num_words[int(i)] + " "    
    
print(out)
    