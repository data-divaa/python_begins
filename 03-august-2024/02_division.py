'''
Authur - Data - Divaa
Date - 03 - august - 2024
question -
        input two integer and write code the logic to print two lines:
        1. the first line should contain the result of integer division a // b ex- 3//5 = 0
        2. the second line contains the result of float division a/ b ex- 3/5 = 0.6

'''


#defining the function
def division(a,b):
    int_div = a // b
    print(int_div)
    float_div = a / b
    print(float_div)

#taking inputs
print("ENTER NUMBER ONLY FOR INTEGER DIVISION AND FLOAT DIVISION ")
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))

#calling function
division(a,b)
