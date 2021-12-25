#Exercise 36

num = int(input("Enter a number: "))

lenght = len(str(num))
total = 0
temp = num

while temp > 0 :
    digit = temp % 10 
    total += digit**lenght
    temp //= 10 # integer division
    
if num == total: 
    print(num,"is an Armstrong number")
else:
    print(num,"is NOT an Armstrong number")
    