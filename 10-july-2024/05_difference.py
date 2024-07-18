'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation difference on them
'''

#defining the function
def difference(list1,list2):
    diff_list = []# taking a empty list fro furthur need
    for i in list1: # we needed range and len for easy accesing of index and value
        if i not in list2:# if ith element of list1 is not present in list2
            diff_list.append(i)# it gets appended into the empty list formed earlier
    diff_set = set(diff_list)#here we are change the list into set we could have did it earlier but working with list much more flexible
    return diff_set

#taking inputs
list1 = list(input("enter the first list ").split())
list2 = list(input("enter the second list ").split())


#calling the function
print(difference(list1,list2))
