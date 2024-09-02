'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question -
you are the managr of a supermarket
you have a list of n items together with their prices that
consumers bought on a particular day.
your task is to print each item_name and net_price
in order f its first occurence
'''
from collections import OrderedDict



#defining the function
def orderdict(l1):
    for k in l1:
        #if item_name is not add the item name and price as key value pair into the empty dictionary
        if k[0] not in d1:
            d1[k[0]] = k[1]
        else:#otherwise add the change the value by addition of price
            d1[k[0]] += k[1]
    for key,value in zip(d1.keys(),d1.values()):
        print(f"{key} {value}")

#taking input
n = int(input("enter the number of records to be entered:"))
d1 = OrderedDict()# a empty dictionary for furthur use
l1 = []
for i in range(n):
    record = input("enter the item name and price space sepearted:")
    record_list = record.split()
    price = int(record_list[-1])#price store the last element also chnaging it to int for furthur use
    item_name = ' '.join(record_list[:-1])#here we store everything other the last one and joining to make it a string
    l1.append([item_name,price])#add them as nested list into the list


#calling the function
orderdict(l1)
