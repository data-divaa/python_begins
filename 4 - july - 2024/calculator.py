'''
Date - 04 - july -2024
Aurthur - Data -Divaa
Question -
        make a calucator for basic arthemtics
'''
# defining a function for calculator
def calculator(num1,num2):
    while True:
        choice = input("enter your choice:      ")
        if choice == 'exit':
            result = "exiting the calculator"
            break
        elif  choice == '-':
            result = num1-num2
            break
        elif choice == '*':
            result = num1 * num2
            break
        elif choice == '/':
            result = num1 / num2
            break
        elif choice == '%':
            result = num1 % num2
            break
        elif choice == '**':
            result = num1**num2
            break
        elif choice == '+':
            result = num1 +num2
            break
        else:
            print("invalid choice")

    return result


print("here the codes--")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for  division")
print("% for floor division (where you get the remainder )")
print("** for exponent")
print("end for stop")



# taking in the numbers
while True:
    num1 = int(input("enter your first number:"))
    num2 = int(input("enter your second number:"))
    print(calculator(num1,num2))
