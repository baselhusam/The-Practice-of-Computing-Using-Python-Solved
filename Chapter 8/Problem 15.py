#Exercise 15

#A)

def palindrome(str1,str2):
    if list(str1) == list(reversed(str2)):
        return True
    else:
        return False
    
print(palindrome('hia', "aih"))

#B)

inp1 = input("Enter the first word: ")
inp2 = input("Enter the second word: ")

if palindrome(inp1, inp2):
    print("word {} and word {} are palindrome.".format(inp1, inp2))
else:
    print("word {} and word {} are NOT palindrome.".format(inp1, inp2))
    
#C)

lst1 = list(inp1.lower())
lst2 = list(inp2.lower())
if " " in lst1:
    lst1.remove(' ')
if " " in lst2:
    lst2.remove(' ')

word1 = " ".join(lst1)
word2 = " ".join(lst2)

if palindrome(word1, word2):
    print("word {} and word {} are palindrome.".format(inp1, inp2))
else:
    print("word {} and word {} are NOT palindrome.".format(inp1, inp2))
