'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation intersection on them
'''

#defining the function
def intersection(list1,list2):
    inter_list = [] # having an empty list
    for i in list1:
        if i not in list2 :#if ith element not in list2
            inter_list.append(i)#it get added to empty list
    for j in list2:
        if j not in list1 :
            inter_list.append(j)# same logic of follows here but with accordance with list2
    inter_set = set(inter_list)#change into set
    return inter_set


#taking inputs
print("intersection represent the elements which are present uniquely on both the sets/n")
list1 = list(input("enter the first list").split())
list2 = list(input("enter the second list").split())

#calling function
print("uniquely present elements in both sets are: ",intersection(list1,list2))