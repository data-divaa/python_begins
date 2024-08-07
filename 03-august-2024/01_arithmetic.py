'''
Authur - Data - Divaa
Date - 03 - august - 2024
question -
        input two integer and write code to print three lines where:
        1. the first line contain contains the sum of two numbers
        2. the second line contains the difference of two numbers (first- second)
        3. the third line contains the product of two numbers
'''


#defining the function
def arithmetic(a,b):
    add = a + b
    print(add)
    sub = a - b
    print(sub)
    mult = a * b
    print(mult)

#taking inputs
print("ENTER NUMBERS ONLY FOR ADDITION,SUBTRACTION,MULTIPLICATION")
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))

#callling function
arithmetic(a,b)
