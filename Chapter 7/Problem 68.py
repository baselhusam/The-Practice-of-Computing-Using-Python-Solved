#Exercise 68

def change(lst,first,second):
    quick = str(lst)
    out = ""
    for i in quick:
        if i == str(first):
            out += str(second)
        else:
            out += i
    return out

L = [3, 2, [3, [[3], 4]]]
print(change(L,3,5))