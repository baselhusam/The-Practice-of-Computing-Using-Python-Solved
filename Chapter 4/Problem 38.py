#Exercise 38

inp = input("Enter a string: ")
out = ""

for i in inp:
    if i.isupper():
        out += i.swapcase()
    else:
        out += i
        
print(out)