#Exercise 25

def digit_count(number):
  even, odd, zeros = 0,0,0
  for i in number:
    if int(i) == 0: #converting the i to integer to do mathmetical operation on it, and to know if it is even or odd
      zeros += 1
    elif int(i) % 2 == 0 :
      even += 1
    else:
      odd += 1
      
  # tuple (even, odd, zeros)   
  return even, odd, zeros #by returning more than one value,
  # they well return as a tuple directly   

number = input("Enter a number: ").split('.')[0] #splitting and take the first element because we want to take the number before the decimal point, and we want it as a string
print(digit_count(number))