#Exercise 22

import math

num = int(input("Enter number: "))
for i in range(2,(int(math.sqrt(num))+1)):
    if num % i == 0:
        print(num,"is NOT a prime number")
        break
else:
    print(num,"is a prime number")