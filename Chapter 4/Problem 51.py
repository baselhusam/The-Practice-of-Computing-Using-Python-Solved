#Exercise 51

inp = input("Enter a sentence here: ")

out = inp[1:-1]

cap,paunc = True, True

if not inp[0].isupper():
    out =inp[0].upper() + out
    cap = False
    
if inp[-1] not in "?!.":
    out += inp[-1] + "."
    punc = False
    
print(out)

if not punc and not cap :
    print("\nwrong format, \nyou have to capitalize the first word and put a punctuation in the last of the sentence.\nthe correct sentnence have to be like that",out)
elif not punc :
    print("\nwrong format, \nyou have put a punctuation in the last of the sentence.\nthe correct sentnence have to be like that",out)
elif not cap :
    print("\nwrong format, \nyou have to capitalize the first word. \nthe correct sentnence have to be like that",out)
elif cap and punc :
    print("\nCorrect format")