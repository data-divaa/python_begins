'''
Date - 8-july-2024
Authur - Data -Divaa
question -
        Write a Python program to get a newly-generated string from a given string where
        "Is" has been added to the front.
        Return the string unchanged if the given string already begins with "Is".
'''
#defining the function
def add_is(string):
    if 'is' not in string: # here if is not present in string its will aded at the front via indexing
        new_string = 'is ' + string[0:]
        return new_string
    elif string.index('is') !=  0:
        a = string.index('is')#the index of is is taken into the variable
        new_string = 'is ' + string[:a] +string[a+2:]# with the help of is index that is is removed and new is is added at the front
        return new_string
    else: # if is is already present at front no changes occur
        return string


#taking inputs
print("enter your string")
string = input()

#calling function
print(add_is(string))
