'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
write a program to take a list as input, as well as 2 index values.
Then swap those two index values with each other, without using a third list
'''

#defining function
def swap(lst,index1,index2):
    # here element at index1 will be replace wityh index2 same follows with index2 and index1
    lst[index1],lst[index2] = lst[index2],lst[index1]
    return lst


#taking inputs
lst = list(input("enter list(separted by sapces) : " ).split())
index1 = int(input("enter index :"))
index2 = int(input("enter index :"))


#calling main function
print(swap(lst,index1,index2))
