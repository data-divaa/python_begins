list1 = [4,1,3,2]
for i in range(len(list1)):
    for a in range(i+1):
        if list1[i] < list1[a]:
            list1[i],list1[a] = list1[a],list1[i]
print(list1)
