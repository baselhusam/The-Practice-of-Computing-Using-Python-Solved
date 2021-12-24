#Exercise 44

from datetime import datetime
from dateutil import relativedelta

date1 = input("Enter the date 1 in Form {yy mm dd}: ").split()
date2 = input("Enter the date 2 in Form {yy mm dd}: ").split()

y1 = int(date1[0])
m1 = int(date1[1])
d1 = int(date1[2])


y2 = int(date2[0])
m2 = int(date2[1])
d2 = int(date2[2])



date1 = datetime(y1, m1, d1)
date2 = datetime(y2, m2, d2)

diff = relativedelta.relativedelta(date2, date1)

years= diff.years
months = diff.months
days = diff.days

print("{} years {} months {} days".format(years, months, days))