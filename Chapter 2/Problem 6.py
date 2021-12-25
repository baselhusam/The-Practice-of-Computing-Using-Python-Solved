#Exercise 6

#Way 1
numbers = list(map(float,input("Enter three numbers to find the largest one: ").split()))

print("The Larges Number is:",max(numbers))


#Way 2
lst = [] #empty list
for i in range(3):
    number = float(input("Enter number: "))
    lst.append(number)
    
print("The Largest Number is:",max(lst))

#Way 3 (without using max function)
lst = []
for i in range(3):
    number = float(input("Enter number: "))
    lst.append(number)
    
max_number = lst[0]
for i in lst:
    if i > max_number:
        max_number = i
        
print("The Largest Number is:",max_number)
