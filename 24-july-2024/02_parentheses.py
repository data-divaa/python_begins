'''
Date - 25 - july - 2024
Author - Data-Divaa
Question -
 Given a string consisting of whitespace and groups of matched parentheses,
 write a Python program to split it into groups of perfectly matched parentheses
 without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
'''


import sys

#defining function
def parentheses(string):
    x = 0
    a = "" # empty string for futher operation
    str_list = [] # empty list for futhur list
    for i in string :
        if i == '(':
            # if above condition comes true x adds +1
            #and same gets added to the empty string
            x = x + 1
            a = a + i
        elif i == ')':
            # if above condition comes true x adds -1
            #and same gets added to the empty string
            x = x - 1
            a = a + i
        else :
            x = x + 0
            # if true literally no chnage happen
            #also nothing is added to a for desirable output
        if x == 0 and i != " ":#if x is 0 and also it is not blank
            str_list.append(a)#then it is treated as an element nd gets added to the list made earlier
            a = ""#this done so to ensure a new blank atring for the entry of new ones


    return str_list



#taking inputs
print("---------ONLY ENTER WHITESPACE OR PARENTHESES----------")
string = input("enter the string : ")
#input validation
for k in string:
    ascii_value = ord(k)
    if not ascii_value == 40 and not ascii_value == 41 and not ascii_value == 32:
        #this is to ensure the data entered is whitespace and parentheses only
        print("---------------------INVALID INPUT -------EXISTING PROGRAM---------------")
        sys.exit()

if string.count('(') != string.count(')'):
    #the above statment is to ensure that the data inputted is matched
    print("---------------------INVALID INPUT -------EXISTING PROGRAM---------------")
    sys.exit()



#calling function
print("after separation concation of string in list :",parentheses(string))
