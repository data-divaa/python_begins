'''
Date = 09 -july-2024
Authur = Data - Divaa
Question -
Write a Python program to calculate the number of days between two dates.
Sample dates (user inputs) : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

months = [31,28,31,30,31,30,31,31,30,31,30,31]
from datetime import datetime
def between_dates(date1,date2):
    date1 = datetime.strptime(a,"%d-%m-%Y")
    date2 = datetime.strptime(b,"%d-%m-%Y")
    month1 = int(date1.strftime("%m"))
    month2 = int(date2.strftime("%m"))

    year1 = int(date1.strftime("%Y"))
    year2 = int(date2.strftime("%Y"))
    diff_year = abs(year2 - year1)
    days = 0
    for i in range(diff_year):

        if (year1 + i ) % 4 == 0 :
            days = days + 1
    for j in range(month1-1,month2+1 ):
        days = days + j
    
    return days



a = input("enter date (dd/mm/yyyy) ")
b = input("enter another date (dd/mm/yyyy) ")


print(between_dates(a,b))
