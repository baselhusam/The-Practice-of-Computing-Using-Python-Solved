#Exercise 16

def sortd(lst):
    if lst == sorted(lst):
        return True
    else:
        return False
    
print(sortd([1,2,3,4])) #True
print(sortd([1,2,3,1])) #False