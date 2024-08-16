'''
Date - 08 - august - 2024
Authur - Data - Divaa
Question -
    given an string ,position, character .
    change the original character of string
    at the given position with the given character

'''

def mutate_string(string,position,character):
    #since string are immutable we first chnage them into list
    string_list = list(string)
    #now with the help of indexing new character replaces the old one
    string_list[position] = character
    #since we need output as a string we again join the list
    string_join = "".join(string_list)
    return string_join


string = input("enter your string : ")
position = int(input("enter the index where change has to be done : "))
character = input("enter the character which is to be replaced in the string : ")

print("after replacing",character,"at",position,"from the original string",string,"the string formed is")
print(mutate_string(string,position,character))
