#Exercise 20

from datetime import date


def convert_to_seconds(inp):
    inp = inp.split('/')
    month = int(inp[0])
    day = int(inp[1])
    year = int(inp[-1])
    
    inp_date = date(year,month,day)
    ques_date = date(year,1,1)
    
    ans_date = inp_date - ques_date
    
    return "{} seconds".format(ans_date.total_seconds())


inp = input("Enter date in this form ( MM/DD/YYYY ): ")
print(convert_to_seconds(inp))