def calculator(num1, num2, op):
    out = 0
    match op:
        case '+':
            out = num1+num2
        case '-':
            out = num1-num2

    return out


print("please input space separated operands - operand1, operand2 ")
user_inp = list(map(int, input().split()))
print("please input operator ")
user_op = input()
print(calculator(user_inp[0], user_inp[1], user_op))
