#Exercise 24

inp = input("Enter a string: ")
prc = input("Enter percantage: ") # EX: 25%

prc = int(prc[:-1]) #delete the % character

prc = prc / 100
end = int(prc * len(inp)) #the index for the last element

print(inp[:end])