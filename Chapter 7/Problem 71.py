#Exercise 71

def solve(str1, str2):
    str3 = str1 +' '+ str2
    
    str3_list = str3.split()
    str3_list.sort()
    return " ".join(str3_list)

f = "work hard" #This could be as input
t = "to reach your goals" #This could be as input
print(solve(f,t))