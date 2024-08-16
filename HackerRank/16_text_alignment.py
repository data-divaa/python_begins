'''
Date - 09 - august - 2024
Authur - Data - Divaa
Question -
    given into thickness and character make H out of it
'''

import sys

#defining the function
def logo(t,c):
    #upper pillar
    for i in range(t):
        #the above line defines for how the the upper pillar will go
        print((c*t).ljust(t*2)+(c*t).rjust(t*2))
        #above line defines the alignment of character
        #with ljust the text align to left with (t*2)
        #same goes for rjust


    #middle belt
    for i in range((t+1)//2):
        #above line defines the thickness as half of t
        print((c*t*4).center(3))

    #lower pillar
    #same logic as upper pillar goes here
    for i in range(t):
        print((c*t).ljust(t*2)+(c*t).rjust(t*2))


#taking inputs
c = input("enter the character through with 'H' logo will be formed: ")
t = int(input("enter the thickness of the logo(make sure the thickness entered is odd): "))
#input validation
if t % 2 == 0:
    print("invalid input.......existing the program")
    sys.exit()

#calling the function
logo(t,c)
