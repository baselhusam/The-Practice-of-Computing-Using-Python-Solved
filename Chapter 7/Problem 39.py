#Exercise 39

lst = [i for i in range(1,101)] #list of numbers from 1 to 100

#A)
print("Sum of even:",sum([i for i in lst if i%2==0]))

#B)
print("Sum of odd:",sum([i for i in lst if i%2 !=0]))