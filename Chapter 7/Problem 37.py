#Exercise 37

L = ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life.']
List1=[[i.upper(), i.lower(), len(i)] for i in L ]

#A)
print(List1)
#[['ALWAYS', 'always', 6], ['LOOK', 'look', 4], ['ON', 'on', 2], ['THE', 'the', 3], ['BRIGHT', 'bright', 6], ['SIDE', 'side', 4], ['OF', 'of', 2], ['LIFE.', 'life.', 5]]

#B)
newlst = [j[0] for j in List1 if j[2] == 4 ]
print(newlst)