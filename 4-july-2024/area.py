'''
Date - 06-july-2024
Authur - Data-Divaa
Question -
        calculating area with given radius
'''

#defing area function
def area(radius):
    result = 3.14 * (radius**2)
    return result

# taking input of radius
radius = float(input("enter the radius of the circle: "))

#calling function
print(" total of circle with",radius,"is",area(radius))
