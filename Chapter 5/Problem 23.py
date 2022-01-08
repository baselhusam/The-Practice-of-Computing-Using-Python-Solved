#Exercise 23

sec = int(input("Enter the number of seconds: "))

def solve(sec):
    times = sec / 10
    begin = 0
    x = 0
    for i in range(11):
        print("At {} secs: {}".format(int(begin),"X"*x))
        begin += times
        x += 1

solve(sec)