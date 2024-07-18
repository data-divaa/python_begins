'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
write a program to take a list as input, as well as 2 index values.
Then swap those two index values with each other, without using a third list
'''
import sys

#defining function
def swap(lst,index1,index2):
    # here element at index1 will be replace wityh index2 same follows with index2 and index1
    lst[index1],lst[index2] = lst[index2],lst[index1]
    return lst


#taking inputs
lst = list(input("enter list(separted by sapces) : " ).split())
print ("the entered list is : ", lst)

index1 = int(input("enter index of the element you want to swap from the above list : "))
#input validation
if (index1 > len(lst)-1):
    print("The entered index is out of bounds...exiting program")
    sys.exit()


index2 = int(input("enter index of the element you want to swap with from the above list : "))
#input validation
if (index2 > len(lst)-1):
    print("The entered index is out of bounds...exiting program")
    sys.exit()

#calling main function
print("The new list after swapping of element ",index1," with ",index2," is : ",swap(lst,index1,index2))
