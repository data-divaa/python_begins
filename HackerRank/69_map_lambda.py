'''
Date - 13 - September- 2024
Aurthur - Data-Divaa
Question -
You have to generate a list of the first N fibonacci number
0 being the first number. Then, apply the map function and a lambda expression
to cube each fibonacci number and print the list.
'''


#defining the function
def fibonacci(n):
    lst = [0,1]
    # if 0 return a blank list
    if n == 0:
        return []
    #if 1 return 0
    if n == 1:
        return [0]
    # we start the loop from 2 upto n and adding the last two digit present in the lst
    for i in range(2,n):
        lst.append(lst[-1]+lst[-2])
    return lst


#taking inputs
n = int(input("enter the number to find the fibonacci numbers upto it:"))


#calling function
#here we print the cube of the fibonacci number with the help of a lambda function
cube = lambda x : [i ** 3 for i in x]
print("the fibonacci numbers upto first ",n,"number",fibonacci(n))
print("the cube of the fibonacci number upto first ",n,"natural numbers is",cube(fibonacci(n)))
