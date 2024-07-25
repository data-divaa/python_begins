'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation difference on them
'''

#defining the function
def difference(list1,list2):
    diff_list = []
    for i in list1:
        if i not in list2: #if i is not in list
            diff_list.append(i)# the element gets added to the empty list formed earlier
    diff_set = set(diff_list)#list converted to set
    return diff_set


print("set difference shows the elements uniquely present in the first set")

list1 = list(input("enter the first set(separated by space) : ").split())
list2 = list(input("enter the second set(separated by space): ").split())

print("first entered set : ",list1)
print("second entered set : ",list2)

print("after the difference operation: ",difference(list1,list2))
