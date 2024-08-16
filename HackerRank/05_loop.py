'''
Authur - Data - Divaa
Date - 04 - august - 2024
Question -
    write code in which take an input n and print the square of that number excluding the number
    i < n and i ** 2
    example - n = 3 i
    [0,1,4]
'''

#defining function
def loop(n):
    for i in range(n):
        print(i ** 2)

#taking inputs
n = int(input("enter the number : "))

#calling function
loop(n)
