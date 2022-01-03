#Exercise 45

from collections import Counter

all_characters = "qwertyuiopasdfghjklzxcvbnm"
inp = input("Enter a string: ").lower()

inp_char = [i for i in inp]

count = Counter(inp_char)

if len(count) == 26:
    print("Yes")
else:
    lst = [key[0] for key in count.items() if key[1]!=0]
    ans = [i for i in all_characters if i not in lst]
    print(' '.join(ans))



