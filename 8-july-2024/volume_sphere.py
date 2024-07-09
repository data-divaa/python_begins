'''
Date - 8-july-2024
Authur - Data -Divaa
question -
        	Write a Python program to get the volume of a sphere with radius six.
'''


#defining function to obtain volume of a sphere
def volume(radius):
    sphere = 4/3 * 3.14 *(radius**3)
    return sphere

#taking radius as input
radius = float(input("enter the raiys of sphere :"))

#calling function
print("volume of sphere with radius ", radius,"is ", volume(radius))
