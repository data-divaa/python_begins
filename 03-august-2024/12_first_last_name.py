'''
Date - 07-august-2024
Authur - Data-Divaa
Question -
        You are given the firstname and lastname of a person on two different lines.
        Your task is to read them and print the following:

    "hello firstname lastname. you just delved into python."

Note - the length of first and last names are each <= 10

'''


import sys
#defining the function
def print_full_name(first_name,last_name):
    print("Hello {} {}! You just delved into python.".format(first_name,last_name))
#here in the above {} is used as a resever and with
#the help of format in sequence the variable are entered with holds the data to be installed

#taking inputs
first_name = input("enter your first name: ")
last_name = input("enter your second name: ")
if len(first_name) != 10 and len(last_name) != 10:
    print("invalid input....existing the program")
    print("you might wanna check the number of character of your string if its within or 10.")
    sys.exit()


#calling function
print_full_name(first_name,last_name)
