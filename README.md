<h1> The-Practice-of-Computing-Using-Python-Solved </h1>

In this repository I will solve  **_The Practice of Computing Using Python_** book the third edition.


<h2> <details><summary> Chapter 1  </summary> </h2>
 <p>

The exercises in this chapter focused on <b> `Variables`, `Math`, `Date`, and `Times` </b>

##  The Used Module to solve the exercises for this chapter:
```python
from datetime import datetime
from dateutil import relativedelta
import calendar
from datetime import date
```
     
 ### The Used Methods for the Modules: 


>1. `datetime` Module
```python
datetime(yy,mm,dd) # to make these numbers in a Time Formula
```

for expanded explanation you can watch this [video](https://www.youtube.com/watch?v=eirjjyP2qcQ) or you can read the [dictionary](https://docs.python.org/3/library/datetime.html)



>2. `realtivedelta` Module

```python
diff = relativedelta.relativedelta(date1,date2)
years = diff.year
months = diff.month
days = diff.days
# Basically it helps us to know the year, month, day for a specific amount of time
```



>3. `calendar` Module
```python
calendar.month(yy,mm)
#To give you the days for that month
```
for expanded explanation you can watch this [video](https://www.youtube.com/watch?v=amFOJMmHk8I) or you can read the [dictionary](https://docs.python.org/3/library/calendar.html)


>4. `date` Module
```python
day = date.today() # The date for this day
```
 </p>
</details>


<h2> <details><summary> Chapter 2  </summary> </h2>
 
 The exercises in this chapter focused on <b> `Control` using `[if statement]` , and `Loops` using `[for, and while loop]`</b>



