#Exercise 28

import string

low = string.ascii_lowercase
lst = [i for i in low] #This list could be as input

newlst,append = [],[]
for i in reversed(lst):
    append =list(i) + append
    newlst.append(append)
    
print(newlst)
