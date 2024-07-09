'''
Date = 09 -july-2024
Authur = Data - Divaa
Question -
Write a Python program to calculate the number of days between two dates.
Sample dates (user inputs) : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

def between_dates(date1,date2):
    date1 = datetime.strptime(a,"%d-%m-%Y")
    date2 = datetime.strptime(b,"%d-%m-%Y")

    diff = date1 - date2
    print("diffrence in days is :")
    return diff.days


from datetime import datetime
a = input("enter date (dd/mm/yyyy) ")
b = input("enter another date (dd/mm/yyyy) ")

print(between_dates(a,b))
