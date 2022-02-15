#Exercise 22

from collections import Counter

def solve(lst):
    count = Counter(lst) #Make dictionary
    key_list = list(count.keys()) #Make a list with keys
    val_list = list(count.values()) #List with values
    sort_val_list = sorted(val_list,reverse=True) #List with sorted value in desceinding order
    out = {} #The output dictionary
    i = 0 #initial value of the idex
    while(len(out.keys())<3): #3 because we want the get the maximum 3 numbers, it will iterate until the output has 3 values or 3 keys in it.
        index = val_list.index(sort_val_list[i]) #The index of the maximum repeatition
        if val_list[index] in out.values(): #if the value is already there we will do something to take the key of the second duplicate value.
            index = val_list.index(sort_val_list[i],i+1,len(val_list)) #start searching to take the index from the place after where we stoped on.
            out[key_list[index]] = val_list[index]#Then make the key and value from that index by taking the key from the key list and value from value list from that specific index
            i += 1 #increase i by on
        else: # If there is no dupilcate in the value then:
            out[key_list[index]] = val_list[index]#Add the number as key and value to the output dictionary
            i += 1 #increase i by one
    
    return out #Return the output dictionary

print(solve([1,2,3,1,2,3,1,4,6,6,1,2,6,1,2,6]))
#The output should be: {1: 5, 2: 4, 6: 4}
