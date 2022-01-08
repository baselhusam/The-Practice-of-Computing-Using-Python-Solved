#Exercise 16

gcd = lambda a,b: a if b == 0 else gcd(b,a%b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The highest common factor between {} and {} is = {}".format(num1,num2,gcd(num1,num2)))