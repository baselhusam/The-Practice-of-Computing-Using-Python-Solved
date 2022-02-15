#Exercise 17

from collections import Counter

d = {}

for i in range(3): #The 3 just random number, it could be 10 etc..
    city = input("Enter a city: ")
    country = input("Enter country: ")
    d[city] = country
    
count = Counter(d.values())
print(count)