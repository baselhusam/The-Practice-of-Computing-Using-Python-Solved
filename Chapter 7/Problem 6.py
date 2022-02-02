#Exercise 6

list1=[1,2,99]
list2=list1
list3=list2
list1=list1.remove(1)
print(list3)

#A) [2,99]


#B) Adding .copy when assignment list1 to list2

list1=[1,2,99]
list2=list1.copy() #HERE IS THE CHANGE
list3=list2
list1=list1.remove(1)
print(list3)
