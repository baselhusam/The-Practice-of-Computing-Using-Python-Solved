#Exercise 21

def solve(begin,end):
    lst = ['1','3','4','8','9'] 
    for i in range(begin,(end+1)): 
        char = [z for z in str(i)] #list with every digit in the number
        flag = True #Checker
        for j in char: #look for every digit in the number
            if j in lst: #check if the digit in the list
                continue
            else: #if its not
                flag = False #Checker go False and break to go to the another number
                break
        if flag: #if the checker didn't go False, that means every digit belongs to the list, so we print it
            print(i)
        
             
A = int(input("Enter the begin of the range: "))                 
B = int(input("Enter the end of the range: "))

if A <= B: #Check whether the begin is less than or equal the end
    solve(A,B)
else:
    solve(B,A)