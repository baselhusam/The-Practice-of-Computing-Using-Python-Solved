#Exercise 29 

import math

num = int(input("Enter an integer greaeter than 2: "))

if num > 2:
    counter = 1
    while num > 2 :
        num = math.sqrt(num)
        print("{}. {:.3f}".format(counter,num))
        counter += 1
        