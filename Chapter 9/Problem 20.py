#Exercise 20
import random

def solve(lst):
    random_numbers = [i for i in range(100)]
    d = {}
    for i in lst:
        d[i] = random.choice(random_numbers)
    return d
