#Exercise 19

def time_format(inp):
    date = inp.split()[0]
    month = int(date.split('/')[0])
    day = int(date.split('/')[1])
    year = int(date.split('/')[-1])
    time = inp.split()[-1]
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    second = int(time.split(":")[-1])
    
    #Check for everything
    if month > 12 or month < 1:
        print("the month should be between 1 and 12")
    if day > 31 or day < 1:
        print("The day should be between 1 and 31")
    if len(str(year)) != 4 :
        print("The year should be contains from 4 digits")
    if hour > 24 or hour < 0:
        print("the hour should be between 0 and 24")
    if minute > 60 or minute < 0:
        print("The minutes should be between 0 and 60")
    if second > 60 or second < 0 :
        print("The seconds should be between 0 and 60")
        
    #A)
    print("{}/{}/{}".format(day,month,year))
    
    #B)
    print("{}:{}:{}".format(hour,minute,second))
    
    #C)
    print("{}/{}".format(month,year))
    
    #D)
    print("PM" if hour>=12 else "AM")
    
    
inp = input("Enter the date and time in this format MM/DD/YYYY HR:MIN:SEC : ")
time_format(inp)
    
    
    
    
    