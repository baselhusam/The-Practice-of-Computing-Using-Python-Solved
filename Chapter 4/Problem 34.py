#Exercise 34

string1 = 'toY'
string2 = 'box'
string3 = "cAr"
string4 = 'to'
integer1 = 2

# (a)
print(string2.upper()) #BOX

#(b) 
print(len(string4)) #2

#(c) 
print(str(integer1).join(string3.swapcase())) #C2a2R

#(d) 
print(string4.index(string1)) # This will include an error, becuase (index) method will produce an errror if the substring was't found in the main string

#(e) 
print(string1.index(string4)) #0

#(f) 
print("string4" in string1) #False