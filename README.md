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

This Chapter focused on `Strings` and how you can solve problems by manipulating the string.
We used a lot of strings methods in this chapter, and here are the summary for them.
### Strings Methods: 

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
### The Used Methods for each Module:
1. `Counter` Module: 
    This module is very helpful for counting and showing the result as a `dictiontry`. For Example:
```python
from collections import Counter

string = "Counter module will count anything you want, words for example or character or symbols .... Anything."
print(Counter(string))
"""
The Output:
Counter({' ': 15, 'o': 9, 'n': 7, 'r': 7, 't': 6, 'e': 5,
         'l': 5, 'a': 5, '.': 5, 'u': 4, 'y': 4, 'm': 3, 
         'w': 3, 'i': 3, 'c': 3, 'h': 3, 's': 3, 'd': 2, 
         'g': 2, 'C': 1, ',': 1, 'f': 1, 'x': 1, 'p': 1, 
         'b': 1, 'A': 1})
"""

#if we wanted to count words:
string = string.split()
print(Counter(string))
"""
The Output:
Counter({'or': 2, 'Counter': 1, 'module': 1, 'will': 1, 'count': 1, 'anything': 1,
         'you': 1, 'want,': 1, 'words': 1, 'for': 1, 'example': 1, 'character': 1, 
         'symbols': 1, '....': 1, 'Anything.': 1})
"""
```

2. `PrettyTable` Module:
    This Module is used for making nice clear tables:
```python
from prettytable import PrettyTable
table = PrettyTable() # To make an empty table
table.field_names = [] # To add Columns names as a "LIST"
table.add_row([]) # To add rows as a "LIST"
print(table)
```

3. `string` Module:
   Simple method made ready variable which make things easier. Some of them:
```python
import string

punc = string.punctuation
lett = string.printable
asc = string.ascii_letters
ascLow = string.ascii_lowercase
ascUpp = string.ascii_uppercase
space = string.whitespace
dig = string.digits
```

<hr>

<h1> Chapter 5 </h1>

This Chapter talked about functions, and the first reason for using or building functions is <b>reusability</b> and it make your code cleaner.
every function should do only one thing.

## Types of Functions in Python

| Type of Functions | Built in Functions | User-Defined Functions (UDFs) |
| :---: | :---: | :---: |
| Example           | <code> print(max(lst)) </code>   | <code> avg = lambda lst: sum(lst) / len(lst) </code> |

## User-Defined Functions (UDFs) devided into two types:
### 1. Return Functions:
functinos have return statement and return a value.
Also you can define a variable with and its value is the return of the function.
#### For Example
```python
def avg(lst):
     return sum(lst)/len(lst)

lst = [1,2,3,4,5,6,7,8,9,10]
average_list = avg(lst)

print(average_list)
"""The output:
   5.5
"""
```
### 2. Procedure Functions:
funtions don't return a thing, it's just make a procedure for the input maybe like adding 5 to a number or anything like that, but doesn't have a return statement.
And you can't define a variable with value of it. Well.... you can, but it will be a none value
#### For Example
```python
def print_elements(lst):
     for i in lst:
          print(lst, end = " ")
          
lst = [1,2,3,4,5,6,7,8,9,10]
elements= print_elements(lst)

print(elements)
"""The Output:
   1 2 3 4 5 6 7 8 9 10 None
"""
```
The `None` shown because the `print_elements` functions doesn't return any value, it's just printing elements without returning any value.


## Scope

This Chapter also talked about the `Scope`.
It's important to understand this concept or you will have errors in your code without knowing how to debugging it.<br>
For Example: If you defined a variable inside a function you <b>can't</b> use it outside the function.
#### For Example:
```python
def avg(lst):
     sum_of_the_list = sum(lst)
     average = sum_of_the_list / len(lst)
     return average
```
if you tried to print the `sum_of_the_list` you will get an error : `name "sum_of_the_list" is not defined`.<br>
So be aware to that, if you defined a variable inside a function you can't use outside the function.

<hr>

<h1> Chapter 6 </h1>

This Chapter talked about `files` and how to work with them.

### File modes:
| Mode | How opened | File Exists | File Does Not Exitst |
| :--: | :--: | :--: | :--: |
| `'r'`| read-only | Opens that file | Error |
| `'w'`| write-only | Clears the file contents | Creates and opens a new file |
| `'a'`| write-only | File content left intact and new data <br> appended at file's end | Creates and opens a new file
| `'r+'`| read and write | Reads and overwrites from the <br> file's beginning | Error |
| `'w+'`| read and write | Clears the file contents | Creates and opens a new file |
| `'a+'`| read and write | File content left intact and read and <br> write at file's end | Creates and opens a new file |

<h1> Chapter 7 </h1>

This Chapters focused on `lists` and `tuples` and the difference between of them.

<h1> Chapter 8 </h1>

In this Chapter we've just implement on functions in advanced way.

     
          
    
               
