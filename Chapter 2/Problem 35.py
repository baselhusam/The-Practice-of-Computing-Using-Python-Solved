#Exercise 35

total,count = 0,0

while total <= 1000:
    num = int(input("Enter number between 1 and 20: "))
    total += num
    count += 1
    print("Total {}".format(total))
    if count > 100:
        break
    