#Exercise 57

hole = ['a','b','d','e','g','o','p']

#A)

def solve_A(string):
    hole_count , else_count = 0,0
    for i in string:
        if i in hole:
            hole_count += 1
        else:
            else_count += 1
            
#B)

def solve_B(words):
    lst = []
    for word in words:
        count = 0 
        for i in word:
            if i in hole:
                count += 1
        if count >= 2 :
            lst.append(word)
            
    return lst



    
    