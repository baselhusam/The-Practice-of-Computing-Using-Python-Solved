#Exercise 31

#Way 1:
input_seconds = int(input("Enter the number of seconds: "))

sec = input_seconds % (24 * 3600)
hours = sec // 3600
sec %= 3600
minutes = sec // 60
sec %= 60

print("{} seconds is {} hours, {} minutes, and {} seconds".format(input_seconds,hours, minutes, sec))

#Way 2: using datatime library
import datetime

input_seconds = int(input("Enter the number of seconds: "))
print(datetime.timedelta(seconds = input_seconds))