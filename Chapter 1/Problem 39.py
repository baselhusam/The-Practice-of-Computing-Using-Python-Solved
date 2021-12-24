#Exercise 39

pass_completions = float(input("To calculate the passer rating please fill the following\nThe pass completions: "))
pass_attempts = float(input("The pass attempts: "))
total_passing_yard = float(input("The total passing yards: "))
interceptions = float(input("The interceptions: "))

C = (pass_completions * 100 - 30 ) / 20
Y = (total_passing_yard - 3) / 4
T = pass_attempts * 20
I = 2.375 - (interceptions * 35)

rating_pass = ((C + Y + T + I) / 6) *100
print(rating_pass)
