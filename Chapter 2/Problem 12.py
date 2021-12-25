#Exercise 12

for year in range(1900,2021):
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                print("{} is a leap year.".format(year))
        else :
            print("{} is a leap year.".format(year))
            