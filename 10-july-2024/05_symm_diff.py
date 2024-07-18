'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation symmetric difference on them
'''


def symm_diff(list1,list2):
    symm_list = []
    for i in list1:
        if i in list1 and i not in list2:# if ith element of list if present in list1 and not in list2
            symm_list.append(i)#then only it gets added to the empty list formed earlier
    for j in list2:
        if j in list2 and j not in list1:
            symm_list.append(j) #same ligic as above foes here
    symm_set = set(symm_list)#conversion to set from list
    return symm_set


#taking inputs
list1 = list(input("enter the first list").split())
list2 = list(input("enter the second list").split())


# calling function
print(symm_diff(list1,list2))
