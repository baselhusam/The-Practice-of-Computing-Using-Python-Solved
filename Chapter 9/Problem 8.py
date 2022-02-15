#Exercise 8

my_dict = {'a':15, 'c':35, 'b':20}

#A)
print(my_dict.keys())

#B)
print(my_dict.values())

#C)
print(my_dict.items())

#D)
for i in sorted(my_dict.keys()):
    print(i, my_dict[i])
    
#E)
key_list =[i for i in my_dict.keys()]
val_list = [i for i in my_dict.values()]

for i in sorted(my_dict.values()):
    pos = val_list.index(i)
    print(key_list[pos], i)