'''
Date - 30 - august- 2024
Aurthur - Data-Divaa
Question - ABC is a ringht triangle at B
therefore angle ABc = 90
point M is the midpoint of hypotenuse AC
you are given the lengths AB and BC.
your task is to find angle MBC in degrees
'''


import math

def angle(AB,BC):
    '''
    since M is the midpoint of AC it implies AM = MC
    also since angle ABC is 90 BM = AC/2= (AM+MC)/2
    BM = (MC+MC)/2
    BM = 2MC/2
    BM = MC
    therefore we canjust get the angke thetha through
    tan = AB/BC
    '''
    #MBC stores the radian value from tan
    MBC = math.atan(AB/BC)
    '''
    we chnage the radian into degree then add chr(176) which
    is the degree symbol with nothing as the seperator
    and finally rounding it off
    '''
    print(round(math.degrees(MBC)),chr(176),sep="")

#taking input
AB = int(input("enter the length of AB:"))
BC = int(input("enter the length of BC:"))

#calling the function
angle(AB,BC)
