'''
Date - 05-july-2024
Authur - Data-Divaa
Question -
        reverse first name and last name with a space between
'''

#definig function
def reverse_name(name):
        rev = " "
    for i in name:  # take up on element of name
        for j in range(len(i)-1,-1,-1): # taking lne of element at i and -1 to gt coorect index now going upto -1 index while going backwards with -1 step
            rev = rev + i[j] # to rev adding jth element of i
        rev = rev + " "# adding space
    return rev
#taking input
name = list(input().split())

#calling the function
print(reverse_name(name))
