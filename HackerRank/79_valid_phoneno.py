'''
Date - 18 - September- 2024
Aurthur - Data-Divaa
Question -
given a integer check whether its a valid phone number that is yen digit and starts with 7,8,9
'''

import re

#defining the function
def valid_phoneno(no):
    ex = r"^[789][0-9]{9}$"
    result = []
    for i in no:
        if re.search(ex,i):
            result.append("YES")
        else:
            result.append("NO")

    for i in result:
        print(i)


#taking inputs
n= int(input("enter the number of phone numbers to check:"))
no = []
for _ in range(n):
    no.append(input("enter the number: "))


#calling thr function
valid_phoneno(no)
