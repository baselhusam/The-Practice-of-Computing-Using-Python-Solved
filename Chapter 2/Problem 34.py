#Exercise 34

for i in range(10000,100000):
    front = str(i)
    front = "1" + front
    front = int(front)
    
    last = str(i)
    last = last + "1"
    last = int(last)
    
    if last / front == 3 :
        print(i)
    