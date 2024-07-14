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



month1 = int(date1.strftime("%m"))
month2 = int(date2.strftime("%m"))
for j in range(month1-1,month2-1 ):


diff_date = abs(date1 - date2).days
days = days + diff_date
