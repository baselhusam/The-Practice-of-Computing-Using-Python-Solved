#Exercise 27

from collections import Counter

filename = input("Enter file name: ")
file = open(filename,"r")

lst = file.read().split()
keys = Counter(lst)

for i in keys.items():
    if i[1] == 1:
        print(i)