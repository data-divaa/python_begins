'''
Date - 20 - September- 2024
Aurthur - Data-Divaa
Question -
you are given css code you ahve to valid hexa color code
'''


import re

#intially having in_css false
in_css = False


n = int(input("enter the number of lines of code :"))
print("start entering the lines:\n")
for i in range(n):
    line = input()
    if '{' in line:
        #if { is found in any line then change the in_css value to True
        in_css = True
    elif '}' in line:
        #once } is found chnage it back to false
        in_css = False
    elif in_css:
        #if in_css is true
        ex = r"#[0-9A-Fa-f]{3,6}"
        #a pattern that in hexanumeric and only between 3 anf 6 length
        for k in re.findall(ex,line):
            #print all the matches of expression and line
            print(k)
