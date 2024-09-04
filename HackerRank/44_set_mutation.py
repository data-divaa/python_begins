'''Date - 03 - September- 2024
Aurthur - Data-Divaa
Question - perform operation based on the input
'''

#defining the function
def mutations(l):
    for i in l:
        command = i[0][0]#for each loop command stores the command extracting it from the nested lists
        s = i[1]#and s stores the set with which opeartion is to be
        if command == "intersection_update":
            A.intersection_update(s)
        elif command == "update":
            A.update(s)
        elif command == "symmetric_difference_update":
            A.symmetric_difference_update(s)
        elif command == "difference_update":
            A.difference_update(s)
    copyA = A
    sum = 0
    for j in A:
        sum = sum + j
    return sum


#taking inputs
n = int(input("enter the number of element in the set A"))
A = set(map(int,input().split()))
n1 = int(input("enter the number of other sets:"))
l = []
print("enter the command and then number of element in the other set then press enter")
print("then enter the set element space seperated and keep on going")
for _ in range(n1):
    command = input().split()
    s = set(map(int,input().split()))
    l.append([command,s])


#calling trh function
print(mutations(l))
