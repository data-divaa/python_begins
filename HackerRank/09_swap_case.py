'''
Date - 07-augusut-2024
Authur - Data-Divaa
Question -
        you are given a string and your task is to swap cases. in other words,convert all lowercase
        letters to uppercase leters and vice versa
'''


#defining the function
def swap_case(string):
    swap_string = ""
    for i in string:
        #checking is the character is upper or lower case
        #if yes then changing it into lower case
        if i.isupper() == True:
            swap_string = swap_string + i.lower()
        #if the character are not is upper case then they are lower
        #then those lower cases will be converted to upper case
        else:
            swap_string = swap_string + i.upper()
    return swap_string


#taking inputs
string = input("enter your string: ")
print("")

#calling the function
print("after converting the uppercase to lowercase and lower to upper the string is :")
print(swap_case(string))
