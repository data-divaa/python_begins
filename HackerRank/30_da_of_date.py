'''
Date - 27- august- 2024
Aurthur - Data-Divaa
Question - take input a date mm - dd- yyyy and print its day in uppercase
'''

import calendar

#defining the function
def day_of_date(m,d,y):
    day_index = calendar.weekday(y,m,d)#this stores the day index
    day_name = calendar.day_name[day_index].upper()#changing that index into name and their chnaging it into upper case
    print(day_name)

#taking input
print("enter the date space seperated mm dd yyyy")
m,d,y = map(int,input().split())

#calling the function
print("the day at the give date is :")
day_of_date(m,d,y)
