#Exercise 13

def make_payment(p):
    if p>=20 and p<= 1000:
        return "Success"
    elif p<20:
        return "Retry. The minimum payment is 20$"
    elif p>1000:
        return "Retry. The credit limit is 1000$"
    
payment = float(input("Enter the payment: "))

print(make_payment(payment))