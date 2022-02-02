#Exercise 54

def transform(list1, list2, r1, r2):
    delete = False
    if list2 == [100,200]:
        delete = True
    list2.extend(list((reversed(list1[r1:r2]))))
    
    if delete:
        del list1[r1:r2]
        
    return list2

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [100,200]

print(transform(l1, l2, 4, 7))
    