import calendar
a = list(input().split())
b = calendar.weekday(a[2],a[1],a[0])
print(b)
