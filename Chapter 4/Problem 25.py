#Exercise 25

brit_word = "flavour"
amer_word = ""

for i in brit_word:
    if i != 'u':
        amer_word += i
        
print(amer_word)