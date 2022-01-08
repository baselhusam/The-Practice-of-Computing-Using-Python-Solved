#Exercise 18


def check_armstrong(num):
    lenght = len(str(num))
    total = 0
    temp = num
    
    while temp > 0 :
        digit = temp % 10 
        total += digit**lenght
        temp //= 10 # integer division
        
    if num == total: 
        print(num,"is an Armstrong number")
        
    
begin = int(input("Enter the begin of the range: "))
end = int(input("Enter the end of the range: "))

for i in range(begin, (end+1)):
    check_armstrong(i)
    