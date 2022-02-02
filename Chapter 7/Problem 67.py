#Exercise 67

def solve(lst):
    for one in range(len(lst)):
        for two in range(one+1,len(lst)):
            for three in range(two+1, len(lst)):
                if lst[one]+lst[two]+lst[three] == 0:
                    return [lst[one],lst[two],lst[three]]   
    else:
        return []
    
lst = [5,1,7,8,-1,0] #This could be as input 
print(solve(lst))