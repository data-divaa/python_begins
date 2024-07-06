'''
Date - 05-july-2024
Authur - Data-Divaa
Question -
        reverse first name and last name with a space between
'''

#defining reverse function for first name
def reverse_first_name(first_name):
    a = ""
    for t in range(len(first_name)-1,-1,-1):
        a = a + first_name[t]
    return a
# defining reverse functin for last name 
def reverse_last_name(last_name):
    b = ""
    for c in range(len(last_name)-1,-1,-1):
        b = b + last_name[c]
    return b


#taking inputs
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")


# callling function)
print(reverse_first_name(first_name),reverse_last_name(last_name))
