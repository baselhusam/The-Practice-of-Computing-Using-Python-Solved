#Exercise 3

for i in range(1,351):
    temp = i
    sum = 0
    while temp > 0 :
        digit = temp % 10
        sum += digit
        temp //= 10
    print(sum)