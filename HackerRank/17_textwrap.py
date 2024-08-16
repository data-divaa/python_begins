'''
Date - 12- august - 2024
Authur - Data - Divaa
Question -
    you are given a string S and with w your task is to wrap the string into a paragraph of width w
'''

#defining the function
def textwrap(s,w):
    #range goes up to the last bit of the string while steping w times
    for i in range(0,len(s)+1,w):
        #print in loop by slicing string from i to i+w also i steps w so it output will not repeat
        print(s[i:i+w])


#taking inputs
s = input("enter your text")
w = int(input("enter the width"))

#calling function
textwrap(s,w)
