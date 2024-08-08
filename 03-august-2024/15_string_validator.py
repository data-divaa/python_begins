'''
Date - 08 - august - 2024
Authur - Data - Divaa
Question -
    given a string check if it is alphanumeric,alphabet,digits,uppercase,lowercase

'''


s = input("enter your string ")
#here any is used t make sure that if any of xth character in s comes true it will print
print(any(x.isalnum()for x in s))
print(any(x.isalpha()for x in s))
print(any(x.isdigit()for x in s))
print(any(x.islower()for x in s))
print(any(x.isupper()for x in s))
