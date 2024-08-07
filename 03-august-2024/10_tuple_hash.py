'''
Date - 06-august-2024
Authur - Data-Divaa
Question -
        given an integer n, and n space-separated integres as input ,
         cretae a tuple t, of those n integers.then  compute and print the result of hash(t).
'''

'''
hash() is used to encrypt hashable(immutable) objects into intger value to avoid cyber threats
'''

import sys


#defining function
def tuple_hash(lst):
    t = tuple(lst)
    return hash(t)



#taking inputs
n = int(input("enter the number of enteries excluding the spaces: "))
lst = list(map(int,input("enter the values space separated: ").split()))
if len(lst) != n:
    print("invalid input .......existing the program")
    print("you might wanna check if the number of enteries and actual enteries match or not ")
    sys.exit()


#calling the function
print("after hashing the value inputted looks like this: ")
print("hash value--",tuple_hash(lst))
#the hashing value differs from version to version
