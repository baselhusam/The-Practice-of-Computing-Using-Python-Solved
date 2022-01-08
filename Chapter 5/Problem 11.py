#Exercise 11

cost = float(input("The cost for that item: "))
member = input("Are you a member? Yes or No? ")

def after_discount(cost,member):
    
  if member == "Yes" or member == "yes" :
    print("the final discounted value for the item:",cost*(15/100))
    print("the final cost for the item after the discount:", cost - cost*(15/100))
    
  elif member == "No" or member == "no" :
    print("the final discounted value for the item:",cost*(5/100))
    print("the final cost for the item after the discount:", cost - cost*(5/100))

after_discount(cost, member)