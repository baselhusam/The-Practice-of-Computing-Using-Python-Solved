#Exercise 4 

score = int(input("Enter the score: "))

if score > 80 :
    print("Grade: A")
elif score >= 60 and score <= 80:
    print("Grade: B")
elif score >= 40 and score < 60:
    print("Grade: C")
elif score > 40:
    print("Grade: D")