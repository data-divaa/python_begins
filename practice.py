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
list1 = list(input("enter the first list ").split())
list2 = list(input("enter the second list ").split())


#calling function
print(union(list1,list2))
