'''
Date - 18-july-2024
Authur - Data -Divaa
question -
is the first letter of the sring is lowercase make it upper lowercase
example - harry potter
--------Harry Potter...also if the string starts with numeric or special charcater leave it as it is
'''

#defining the function
def capitalize(string):
    lst = string.split()#spilting the string into list
    l1 = []
    for i in lst:
        if i[0].islower():#if the first letter of element is lowercase
            cap = i[0].upper()#cap will store the uppercase version of first letteer of element
            new_i = cap +i[1:]#now the element with the uppercase will be stored in new_i with the help of slicing
            l1.append(new_i)#appending these two into l1
            l2 = " ".join(l1)#list is turned into string
        elif i[0].isdigit():#if the first letter of element is digit then
            l1.append(i)
            l2 = " ".join(l1)
            #print the same
        else:
            pass
    print(l2)

#taking inputs
string = input("enter the string whose first character is to changed into uppercase: ")

#calling the function
capitalize(string)
