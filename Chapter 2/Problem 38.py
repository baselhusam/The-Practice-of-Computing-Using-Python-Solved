#Exercise 38

num = int(input("Enter a number: "))
sum = 0

if num <= 0 :
    print("Enter a positive number")
else:
    for i in range(1,num+1):
        sum += i
        
print("Sum of the first {} natural numbers is: {}".format(num,sum))
