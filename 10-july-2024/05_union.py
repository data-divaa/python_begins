'''
Date - 15 - july - 2024
Author - Data-Divaa
Question -
Take two lists from user as input. Perform set operation union on them
'''

#defining function
def union (list1,list2):
    union_list = []# having an empty list
    for i in list1:
        union_list.append(i)# adding all the elements to a new list for ease
        if union_list.count(i) != 1: # if ith element of list1 is more than 1 times
            union_list.remove(i)#then it get removed
    for j in list2:
        union_list.append(j)
        if union_list.count(j) != 1:
            union_list.remove(j)#same logic as above
    union_set = set(union_list)#change into set
    return union_set


#taking inputs
print("union of set presents a set which have all the elements present in both the set eliminating duplicates")
list1 = list(input("enter the first list ").split())
list2 = list(input("enter the second list ").split())


#calling function
print("common elements of both the sets are: ",union(list1,list2))
