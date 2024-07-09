'''
Date - 8-july-2024
Authur - Data -Divaa
question -
        		Write a Python program to calculate the difference between a given number and 17.
            If the number is greater than 17, return twice the absolute difference.
'''


#defining function
def difference_17(number):
    if number > 17 :#if number taken is greater than 17 the diifernece will be twice
        result = (number -17) * 2
    else:
        result = number -17
    return result
#taking inputs
int_float = input("enter the data type of number(int or float):  ")
if int_float == "int":
    number = int(input("enter the number: "))
elif int_float == "float":
    number = float(input("enter the number; "))
else:
    print("invalid choice")

#calling function
print(difference_17(number))
