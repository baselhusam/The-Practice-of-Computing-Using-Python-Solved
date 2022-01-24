#Exercise 10

one, two, three = map(int,input("Enter three numbers: ").split())

try:
    result = (one / two) + three
    print(result)
except ZeroDivisionError:
    print("You can't divide number to a zero.")
except ValueError:
    print("You should input numbers not string.")
    