'''
Date - 18 - September- 2024
Aurthur - Data-Divaa
Question -
you are given string check if the string entered is a valid roman number if yes
print true is not print false
'''

import re

def valid_roman(string):
    th = r"M{0,3}"#match with M,MM,MMM
    hun = r"(CD|CM|D?C{0,3})"#match with CD CM D(optional) and C can't be more than 3
    tenth = r"(XC|XL|L?X{0,3})"
    one = r"(IX|IV|V?I{0,3})"
    regex_pattern = r"%s%s%s%s$" % (th,hun,tenth,one)#here %s act as a place holder
    print(str(bool(re.match(regex_pattern, string))))


string = input("enter your string(must be uppercase)")
for k in string:
    ascii = ord(k)
    if not(65 < k < 90):
        print("you entered lower case")
        sys.exit()

print("is",string,"a roman number")
valid_roman(string)
