'''
date - 06 - august - 2024
authur - data - divaa
question -
    consider a list = [] and perform the following operation
    1.    insert i e: Insert integer e at position i .
    2. print : print the list
    3. remove e: delete the frst occurence of intger e
    4. append e : insert integre e at the end of the list
    5.sort : sort the list
    6. pop : pop the last element from the list
    7.reverse :reverse the list

Initialize your list and read in the value of followed by lines
of commands where each command will be of the types listed above
.Iterate through each command in order and
perform the corresponding operation on your list


example -
input = n = 4
        append 1
        append 2
        insert 3 1
        print

output  = [1,3,2]
explanation =
- n= 4 four lines to do operation
- append 1 = append 1 to the list
- append 2 = append 2 to the list
-insert 3 1 = insert 3 at index 1
- print = print the list
'''
import sys
def lists(N):
    a = []
    for i in range(N):
        command = input().split()
        a.append(command)
    result = []
    for k in a:
        if 'insert' in k:
            result.insert(int(k[1]),int(k[2]))
        elif 'remove' in k:
            result.remove(int(k[1]))
        elif 'append' in k:
            result.append(int(k[1]))
        elif 'sort' in k:
            result.sort()
        elif 'pop' in k:
            result.pop()
        elif 'reverse' in k:
            result.reverse()
        elif 'print' in k:
            print(result)
        else:
            print("invalid input .....exisiting program")
            sys.exit()


N = int(input("enter the lines"))
lists(N)
