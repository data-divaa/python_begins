'''
Date - 15 - September- 2024
Aurthur - Data-Divaa
Question -
define a function to check if a email is valid or not if yes print in lexicographical order
'''


import re
import sys

emails = []
n = int(input("enter the number of emails to be entered:"))
for _ in range(n):
    emails.append(input())



#defining the function
def valid_email(emails):
    #here a pattern is defined
    ex = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    result = []
    for i in emails:
        if re.search(ex,i):#if the email match with the expression
            result.append(True)
        else:
            result.append(False)

    for i in result :
        if i == False:
            print("email entered is not valid")
            sys.exit()
        else:
            #if all the emails are valid then sort them
            sorted_emails = sorted(emails)
    for k in sorted_emails:
        print(k,"- valid")



#calling the function
valid_email(emails)
