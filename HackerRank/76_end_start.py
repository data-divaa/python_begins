'''Date - 18 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a string s .
your task is to find the indices of the start and end of string k in s.
if no match is found print (-1,-1)
'''

import re

def start_end_index(s,k):
    ex = rf"(?=({k}))"
    match = re.finditer(ex,s)
    result = []
    for i in match:
        result.append((i.start(),i.start()+len(k)-1))
        '''here we do not use end() because we are using ?=(lookahead)
        and lookahead do not consume character hence end() will not work'''
    if result:
        for k in result :
            print(k)
    else:
        print((-1,-1))

s = input("enter the string where substring is to be checked:")
k = input("enetr the substring to check the in the string:")

print("the start ad end index of matched substring are:")
start_end_index(s,k)
