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

def parentheses(string):
    lst = []
    for i in string :
        ascii_value = ord(i)
        if ascii_value == 40:
            lst.append(ascii_value)
            if ascii_value == 41:
                lst.append(ascii_value)
    return ascii_value

string = input("").split()

print(parentheses(string))
