#Exercise 32

def checklen(x):
    if len(str(x)) == 3:
        return True
    else:
        return False
    
def checkdigits(x,square):
    x = str(x)
    square = str(square)
    if x[0] == square[-2] and x[1] == square[-1]:
        return True
    else:
        return False


for i in range(10,100):
    square = i*i
    if checklen(square):
        if checkdigits(i, square):
            print(i)
            
#The answer is 25
            
            