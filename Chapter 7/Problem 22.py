#Exercise 22

lst = [10,20,30,40,50] #This list could be as an input
newlst= []
for i in range(len(lst)):
    if i == 0: #first element 
        newlst.append(lst[i]+lst[i+1])
    elif i == len(lst)-1: #last element
        newlst.append(lst[i]+lst[i-1])
    else: #elements in between
        newlst.append(lst[i-1]+lst[i]+lst[i+1])
        
print(newlst)
