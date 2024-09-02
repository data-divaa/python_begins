'''
Date - 29 - august- 2024
Aurthur - Data-Divaa
Question - print the difference between two time in seconds
'''

from datetime import datetime,timedelta

#defining the function
def time_delta(time_list):
    #setting up the format for further used
    '''
    a-day name
    d - month
    b- date
    Y- year
    H- hour
    M- minutes
    S-seconds
    z- time zone
    '''
    date_format = "%a %d %b %Y %H:%M:%S %z"
    for k in time_list:
        '''since time_list contain nested list we take first one
        then by index change the string into date in the same format as seted earlier
        '''
        time1 =  datetime.strptime(k[0],date_format)
        time2 =  datetime.strptime(k[1],date_format)
        '''here first subtract the two time then since the output is
        in minute we change it into seconds but since we need it in seconds
         and since the subtract can add sign we we store the absoulte value only
         '''
        diff =  abs((time1-time2).total_seconds())
        print(int(diff))



#taking input
t = int(input("enter the pair of time you want to enter:"))
time = []
time_list = []
for i in range(t):
    t1 = input()
    t2 = input()
    time.append([t1,t2])
    time_list.append(time)
    time = []

#calling the function
time_delta(time_list)
