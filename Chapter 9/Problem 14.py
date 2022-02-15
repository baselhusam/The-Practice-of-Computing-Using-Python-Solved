#Exercise 14

from collections import Counter
import matplotlib.pyplot as plt

#A)
def solve_a():
    inp = input("Enter a string here: ")
    count = Counter(list(inp))
    del count[' ']
    keys_list = count.keys()
    val_list = count.values()
    index = val_list.index(max(val_list))
    return keys_list[index]

#B)
def solve_b():
    inp = input("Enter a string here: ")
    count = Counter(list(inp))
    del count[' ']
    return count

#C)
def solve_c():
    inp = input("Enter a string here: ")
    count = Counter(list(inp))
    del count[' ']
    print(count)
    plt.hist(count)
    plt.show()
