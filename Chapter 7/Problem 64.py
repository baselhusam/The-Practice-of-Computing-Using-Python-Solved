#Exercise 64

lst = []
ln = 0

while True:
    if ln == 5:
        break
    
    num = input("Enter integer or exit: ")
    if num == "exit":
        break
    
    lst.append(int(num))
    ln += 1
    
print(lst)
