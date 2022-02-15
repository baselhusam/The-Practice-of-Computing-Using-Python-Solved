#Exercise 4

D = {'a':3,'x':7,'r':5}

#A)
print(D['x'])

#B)
key_list = list(D.keys())
val_list = list(D.values())

position = val_list.index(7)
print(key_list[position])