'''
Date - 05 - july- 2024
Authur - Data - Divaa
Question -
        make a calculator through switch case
'''
# defining calculator through switch case
def calculator(num1, num2, op):
    out = 0
    match op:
        case '+':
            out = num1+num2
        case '-' :
            out = num1-num2
        case '*' :
            out = num1*num2
        case '/' :
            out = num1/num2
        case '**' :
            out = num1**num2
        case '%' :
            out = num1 % num2
    return out

#taking inputs
print("please input space separated operands - operand1, operand2 ")
user_inp = list(map(int, input().split()))
print("")
print(" + --- addition \n - --- subtraction\n * --- multiplication\n / --- division\n ** --- exponent\n % --- floor division\n end --- exit")
print("")
print("please input operator ")
user_op = input()
print(calculator(user_inp[0], user_inp[1], user_op))
