#Exercise 38

number = 6 #This could be as input 

def sum_factor(num):
    return sum([i for i in range(1,num+1) if num % i == 0])

print(sum_factor(number))