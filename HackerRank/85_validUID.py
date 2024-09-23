'''
Date - 23 - September- 2024
Aurthur - Data-Divaa
Question -
check if the uid of empolyess is valid or not
the valid uid must follow thw follwoing rules :
- at least 2 uppercase englsih alphabet
- must contain at least 3 digits (0-9)
- should only contain alphanumeric
- no character should repeat
- there must be exactly 10 characterin a valid UID
'''


import re


#defining inputs
def valid_UID(IDs):
    ex = r"^(?!.*(.).*\1)(?=(.*[A-Z]){2,})(?=(.*[0-9]){3,})[A-Za-z0-9]{10}$"

    result = []
    for i in IDs:
        if re.search(ex,i):
            result.append("Valid")
        else:
            result.append("Invalid")
    for k in result :
        print(k)



#taking inputs
n = int(input("enter the number of code:"))
IDs= []
for _ in range(n):
    IDs.append(input())


#calling the function
valid_UID(IDs)
