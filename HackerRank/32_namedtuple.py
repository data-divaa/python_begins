'''
Date - 28- august- 2024
Aurthur - Data-Divaa
Question - input is student id ,marks ,class,name
now you gotta print their average
'''
from collections import namedtuple

sum = 0
n = int(input("enter the number of records of students:"))
record_list=[]
columns = input("enter the column name ").split()
for i in range(n):
    record = input().split()
    #add each of the record to a list
    record_list.append(record)
data = namedtuple('data',columns)#create a namedtuple data with column names as taken
for k in record_list:
    values = data(*k)#assign the record as values for the namedtuple
    sum = sum + int(values.mark)#add the values stored in the marks in the namedtuple
average = sum /n
print({:2f}.format(average))#only decimal 
