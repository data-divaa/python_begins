'''
Date - 07-august-2024
Authur - Data-Divaa
Question -
        You are given a string. Split the string on a " " (space) delimiter
        and join using a - hyphen.
'''

#defining the function
def split_and_join(line):
    line_split = line.split(" ")
    #in the above line string entered is splited and formed into a element of a list whereever space comes
    line_join = "-".join(line_split)
    #in the above line the list formed through spliting is joined through hyphen
    #all the element of list are joined.
    return line_join

#taking input
line = input("enter the string: ")
print("")

#calling function
print("after spliting the string and then joining them with hyphen the new string formed is ")
print(split_and_join(line))
