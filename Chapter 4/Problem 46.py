#Exercise 46

alph = "abcdefghijklmnopkrstuvwxyz"

inp = input("Enter a note here to enctypt it: ").lower()

out_letters = []

for i in inp:
    ind = 25 - alph.find(i)
    out_letters.append(alph[ind])
    
out = ''.join(out_letters)
print(out)

