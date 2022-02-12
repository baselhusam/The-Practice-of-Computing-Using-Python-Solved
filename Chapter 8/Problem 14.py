#Exercise 14

#A)
def solve(str1,str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
print(solve("silent","listen"))

#B)

inp1 = input("Enter the first word: ")
inp2 = input("Enter the second word: ")

if solve(inp1,inp2):
    print("The {} word and the {} word are Anagrams.".format(inp1,inp2))
else:
    print("The {} word and the {} word are NOT Anagrams.".format(inp1,inp2))