'''
Date - 05 - july- 2024
Authur - Data - Divaa
Question -
        make a calculator through switch case
'''

#definig addition function
def add():
    return num1 + num2

#defining subtraction function
def sub():
    return num1 - num2

#defiing multiplication function
def multi():
    return num1 * num2

#definig division function
def div():
    return num1 / num2

#defining exponent function
def expo():
    return num1 ** num2

#defining floor division function
def floor():
    return num1 % num2

#defining exit function
def exit():
    return "existing the calculator"

#defing default function
def default():
    return "invalid choice"


#calling the calculator function
def calculator(choice):

    switch = {
        '+' : add,
        '-' : sub,
        '*' : multi,
        '/' : div,
        '**': expo,
        '%' : floor,
        'end' : exit
        }
    #comment
    '''
    get - used to associated key (here choice) and value (here function) if available
    default - is nothing matches default will work
    () - to call function called through switch.get(choice)
    '''
    #return statement
    return switch.get(choice,default)()


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
