#Exercise 14

def calc(num1,num2,op):
    if op == "+":
        return "{} + {} = {}".format(num1,num2,num1+num2)
    elif op == "-":
        return "{} - {} = {}".format(num1,num2,num1-num2)
    elif op == "*":
        return"{} x {} = {}".format(num1,num2,num1*num2)
    elif op == "/":
        return "{} / {} = {}".format(num1,num2,num1/num2)
    else:
        return "Unsupported operation. TRY AGAIN."




num1 = float(input("Enter the first number: "))
op = input("Enter the operator ( +  -  *  / ): ")
num2 = float(input("Enter the second number: "))

print(calc(num1,num2,op))
