#Exercise 72

file_name = input("Enter your file path: ")

file = open(file_name,"r")
num_of_words = 0
len_of_words = 0

for words in file:
    for word in words.split():
        num_of_words += 1
        len_of_words += len(word)
        
avg = len_of_words / num_of_words

print("number of words:",num_of_words,"word")
print("average word lenght: {:.2f} letter".format(avg))