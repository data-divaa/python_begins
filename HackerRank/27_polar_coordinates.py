'''
Date - 26- august- 2024
Aurthur - Data-Divaa
Question - take input of complex number and print the distance and phase
'''
import cmath

#defining the function
def coordinates(ordinates):
    #since we took input as string needed to change it into complex
    complex_coordinate = complex(ordinates)
    #nw sqrt for square real and imag to take those specific path and lastly abs to just the real value
    distance = abs(cmath.sqrt(complex_coordinate.real**2 + complex_coordinate.imag**2))
#phase is inbulit function used to have the angle betwwen the the coordinated
    phi = cmath.phase(complex_coordinate)
    print("the distance is : ",distance)
    print("the phase angle is" ,phi)

#taking the input
ordinates = input("enter the complex number:")

#callling the function

coordinates(ordinates)
