#Excercise 8

def sum_primes(lower,upper):
    #Start of the Sieve Algorithm
    lst = [True] * (upper+1)
    lst[0] = lst[1] = False
    for i in range(2,(upper+1)):
        if lst[i]:
            for j in range(i*i,(upper+1),i):
                lst[j] = False
    #End of the Sieve Algorithm
    
    #Start to take prime number from the wanted range
    sum = 0
    for i in range(lower,(upper+1)):
        if lst[i]:
            sum += i
            
    return "The sum for prime number from range {} to {} is: {}".format(lower,upper,sum)


low = int(input("Enter the lower limit: "))
up = int(input("Enter the upper limit: "))

print(sum_primes(low, up))