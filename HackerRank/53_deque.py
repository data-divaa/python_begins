'''
Date - 06 - September- 2024
Aurthur - Data-Divaa
Question -
Perform append, pop, popleft and appendleft methods on an empty deque
'''
from collections import deque


#defining trh function
def deque_opeartions(command):
    lst = deque()
    for i in command:
        if i[0] == "append":
            lst.append(i[1])
        elif i[0] == "appendleft":
            lst.appendleft(i[1])
        elif i[0] == "pop":
            lst.pop()
        elif i[0] == "popleft":
            lst.popleft()
        else:
            pass
    result = ' '.join(lst)
    return result

#taking input
n = int(input())
command = []
print("in the below lines first write the command(pop,popleft,append,appendleft) and the value :")
for _ in range(n):
    command.append(input().split())

#function call
print("after all the operation elemnt left in the list is ")
print(deque_opeartions(command))
