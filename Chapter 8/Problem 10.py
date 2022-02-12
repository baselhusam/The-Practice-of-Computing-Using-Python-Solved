#Exercise 10

def solve(lst):
    if min(lst) == max(lst):
        return min(lst)
    else:
        return min(lst),max(lst)
    
print(solve([1,2,3,4,5]))
print(solve([7,7,7,7,7]))
