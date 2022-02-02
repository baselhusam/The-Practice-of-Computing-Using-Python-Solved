#Exercise 47

def solve(string):
    lst = [i for i in string]
    lst.sort()
    return "".join(lst)

inp = "what is your name"
print(solve(inp))
print(type(solve(inp)))