#Exercise 7

# use this string as an input : "python python is great great and great and jave is also jave amazing great

#Way 1

from collections import Counter


inp = input("Enter a sequence of words: ").split()
uniq = Counter(inp)

print(' '.join(uniq.keys())) #joining the keys as a string
# __________________________________________



#Way 2 (without using any external library)
inp = input("Enter a sequence of words: ").split()
lst = []

for i in inp: # for looking for each word
    if i not in lst: # To check the word if its not duplicated
        lst.append(i) # if yes append it to the list
        
print(' '.join(lst)) # joining the list using ' '.join(lst)
# __________________________________________


#Way 3 (shorter implementation)
inp = input("Enter a sequence of words: ")
print(' '.join(dict.fromkeys(inp.split()))) 
# make a dictionary from the list then take the keys which are the not duplicate words and the joining them as a string
# __________________________________________ 

