#Exercise 7

def right_angled(a,b,c):
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        return "The triangle is right-angled."
    else:
        return "The triangle is not right-angled."