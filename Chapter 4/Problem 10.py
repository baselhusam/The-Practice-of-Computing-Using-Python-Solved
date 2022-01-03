#Exercise 10

S= "I had a cat named amanda when I was little"

count = 0
lenght = len(S)
i = 0

while i < lenght:
    if S[i] == 'a':
        count += 1
    i += 1
    
print(count)

