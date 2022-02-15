#Exercise 21

from collections import Counter

def solve(string):
    count = Counter(list(string.lower()))
    return [i for i in count.keys() if count[i] == 1]
