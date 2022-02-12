#Exercise 5

def my_function(lst,index,operation):
    if operation == "pop":
        del lst[index]
        return lst
    elif operation == "insert":
        lst.insert(index,"new element")
        return lst
    else:
        return "Please input an approperiate operation."
        
# Example:
# lst = [1,2,3,4,5,6,7,8]
# print("POP:",my_function(lst, 2, "pop"))
# print("INSERT:",my_function(lst, 5, "insert"))