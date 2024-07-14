'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
write a program to take a list as input, as well as 2 index values.
Then swap those two index values with each other, without using a third list
'''


def swap(lst,index1,index2):
    # interchange
    lst[index1],lst[index2] = lst[index2],lst[index1]
    return lst

lst = list(input("list: " ).split(','))
index1 = int(input("enter index :"))
index2 = int(input("enter index :"))

print(swap(lst,index1,index2))
