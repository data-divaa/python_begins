'''
Date - 23 - September- 2024
Aurthur - Data-Divaa
Question -
you are given some credit card number and you have to check if they are valid or not
'''


import re


#defining the function
def valid_creditcard(cards):
    ex = r"^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$"
    #this expresion checks if the card number starts with 4,5,6 or have 4- encounters
    result = []
    for i in cards:
        if  not re.match(ex,i):#if the expression is not match
            result.append("Invalid")
        else:#now only is the expression is matched
            i = i.replace("-","")#replace - with blank
            if len(i) != 16:#if the length of the number is above 16 print invalid
                result.append("Invalid")
            elif re.search(r"(\d)\1{3,}",i):#if any digit is repeated more than 3  times print invalid
                result.append("Invalid")
            else:#else print valid
                result.append("Valid")

    for k in result:
        print(k)


#taking inputs
cards = []
for _ in range(int(input("enter the number of credit card numbers:"))):
    cards.append(input())

#calling function
valid_creditcard(cards)
