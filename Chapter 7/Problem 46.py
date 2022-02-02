#Exercise 46

import numpy as np

l1 = list(np.random.randint(1,100,size=(25)))
l2 = list(np.random.randint(100,200,size=(25)))

l1.sort()
l2.sort()

l3 = l1 + l2
print(l3)