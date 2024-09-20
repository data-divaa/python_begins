'''
Date - 19 - September- 2024
Aurthur - Data-Divaa
Question -
take emails and check is they are valid if yes
print their name and email address in the sequence as they were entered
'''

import email.utils
import re


#defining the function
def valid_email(record):
    ex = r'^[a-zA-Z][a-zA-Z0-9-_\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    valid_record = []
    for name,mail in record:
        if re.search(ex,mail):#if the mail part of the tuple matches
            valid_record.append((name,mail))#add that name and mail to the list

    for i in valid_record:
        #printing the elements in list after chnaging them into string from tuple
        print(email.utils.formataddr(i))



#taking inputs
n = int(input("enter the number of email addrerss entered for validations:"))
record = []
for _ in range(n):
    #taking the input and changing it into a tuple and adding it to the list
    info = email.utils.parseaddr(input())
    record.append(info)


#calling function
print("valid username and emails are:")
valid_email(record)
