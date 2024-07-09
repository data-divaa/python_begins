'''
Date - 05 - july- 2024
Authur - Data - Divaa
Question -
        make a calculator through switch case
'''




# taking arithemtics choice
print(" + --- addition \n - --- subtraction\n * --- multiplication\n / --- division\n ** --- exponent\n % --- floor division\n end --- exit")



#input of numbers
while True:
    choice = input("enter your choice:  ")
    print("")
    num1 = float(input("enter number:  "))
    print("")
    num2 = float(input("enter another number "))
    print("")
    print(calculator(choice))


print(reversing_name(first_name),reversing_name(last_name))
