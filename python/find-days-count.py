year = int(input())
month = int(input())
if month == 1 or    month == 3 or    month == 5 or  \
    month == 7 or     month == 8 or   month == 10 or  \
    month == 12:
    days = 31
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or \
        (year % 400 == 0):
        days = 29 
    else:
        days = 28 
else:
    days = 30 
print(f'{days} Days')