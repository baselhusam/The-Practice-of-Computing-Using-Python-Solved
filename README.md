<h1> The-Practice-of-Computing-Using-Python-Solved </h1>

In this repository I will solve  **_The Practice of Computing Using Python_** book the third edition.


# Chapter 1

The exercises in this chapter focused on <b> `Variables`, `Math`, `Date`, and `Times` </b>

## The Used Module to solve the exercises for this chapter:
```
from datetime import datetime
from dateutil import relativedelta
import calendar
from datetime import date
```

## The Used Methods for the Modules:

>1. `datetime` Module
```
datetime(yy,mm,dd) # to make these numbers in a Time Formula
```

>2. `realtivedelta` Module
```
diff = relativedelta.relativedelta(date1,date2)
years = diff.year
months = diff.month
days = diff.days
# Basically it helps us to know the year, month, day for a specific amount of time
```

>3. `calendar` Module
```
calendar.month(yy,mm)
#To give you the days for that month
```

>4 `date` Module
```
day = date.today() # The date for this day
```


