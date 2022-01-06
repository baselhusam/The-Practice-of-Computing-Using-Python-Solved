<h1> The-Practice-of-Computing-Using-Python-Solved </h1>

In this repository I will solve  **_The Practice of Computing Using Python_** book the third edition.


<h1>  Chapter 1  </h1>

The exercises in this chapter focused on <b> `Variables`, `Math`, `Date`, and `Times` </b>


     
### The Used Methods for each Module: 

1. `datetime` Module
```python
from datetime import datetime
  
datetime(yy,mm,dd) # to make these numbers in a Time Formula
```

for expanded explanation you can watch this [video](https://www.youtube.com/watch?v=eirjjyP2qcQ) or you can read the [dictionary](https://docs.python.org/3/library/datetime.html)



2. `realtivedelta` Module

```python
from dateutil import relativedelta
  
diff = relativedelta.relativedelta(date1,date2)
years = diff.year
months = diff.month
days = diff.days
# Basically it helps us to know the year, month, day for a specific amount of time
```



3. `calendar` Module
```python
import calendar 
 
calendar.month(yy,mm)
#To give you the days for that month
```
for expanded explanation you can watch this [video](https://www.youtube.com/watch?v=amFOJMmHk8I) or you can read the [dictionary](https://docs.python.org/3/library/calendar.html)


4. `date` Module
```python
from datetime import date

day = date.today() # The date for this day
```
<hr>

 <h1> Chapter 2   </h1>
 
 The exercises in this chapter focused on <b> `Control` using [`if statement`] , and `Loops` using [`for, and while loop`]</b>
 
 ### The Used Methods for each Module:
 
 1. `Random` Module
 ```python
 import random
 
 choices = ['a','b','c']
 choice = random.choice(choices)
 # this command chose a random element from a list, in this case it could be (a or b or c)
 ```
 <hr>
 
 <h1> Chapter 3 </h1>
 
 This Chapter talked about algorithms and how algorithm should be:
 - Detailed 
 - Effictive
 - Specefic 
 - General Purpose
 
 And the Program should be:
 - Readable
 - Robust
 - Correct

<hr>

<h1> Chapter 4 </h1>

This Chapter focused on `String` and how you can solve problems by manipulatin the string.
We used a lot of string methods in this chapter, and here is the summary for them.
<h4> String Methods </h4>
```python
string = " Hi, I am using Python "
char = 'B'

string.capitalize() # Hi, i am using python
string.upper() # HI, I AM USING PYTHON
string.lower() # hi, i am using python
string.replace('i','c') # Hc, I am uscng Python
string.lstrip() #Hi, I am using Python
string.rstrip() # Hi, I am using Python
string.strip() #Hi, I am using Python
string.count('am') #1
string.index('u') #10
string.find('o') #20 
string.split() #['Hi,', 'I', 'am', 'using', 'Python']
string.swapcase() # hI, i AM USING pYTHON

char.islower() #False
char.isupper() #True
char.swapcase() #b
char.isspace() #False
char.isalnum() #True
char.isdigit() #False
char.isalpha() #True

```


