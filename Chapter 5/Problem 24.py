#Exercise 24

def sort(lst):
    lst.sort()
    return " ".join(lst)


words = input("Enter strings seperated by space: ").lower().split()
print(sort(words))