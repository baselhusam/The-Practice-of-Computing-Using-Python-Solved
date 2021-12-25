#Exercise 18

#A)
num = int(input("Enter number here: "))
total = 0

for i in range(1,num+1):
    total += i
    
print("The sum of {} is: {}".format(num,total))


#B)
num = int(input("Enter number here: "))
total = 0

for i in range(1,num+1):
    total += i
    print(total)
   
    
#C)
num = int(input("Enter number here: "))
total = 0

for i in range(1,num+1):
    total += i

if total % num == 0:
    print("The sum of {} is: {}".format(num,total))
