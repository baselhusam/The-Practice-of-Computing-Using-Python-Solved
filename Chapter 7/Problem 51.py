#Exercise 51

def mini(lst):
    minn = lst[0]
    for i in lst:
        if i < minn:
            minn = i
    return minn
            
def maxi(lst):
    maxx = lst[0]
    for i in lst:
        if i > maxx:
            maxx = i
    return maxx    
    

lst = [1,2,5,7,9,15,30,55,0]

print(mini(lst))
print(maxi(lst))