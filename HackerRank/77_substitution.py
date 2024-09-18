'''
Date - 18 - September- 2024
Aurthur - Data-Divaa
Question -
given line of string when encountered " && " replace it to and
and when ' || ' replace it to or and these must not be in the end or start of the line
'''


import re

#defining the sub function
def change(s):
    if s.group(1) == "&&":
        return "and"
    elif s.group(1) == "||":
        return "or"
    else :
        return s


'''
here we define a pattern which look for ' && ' or ' || '
when found the match is send to the change function the the match at group(1) that the only the && and ||
will be switched out with and or not the spaces
'''


#defining the main function
def substitution(lines):
    ex = r"(?<=\s)(\|\||&&)(?=\s)"
    output= []
    for i in lines:
        check = re.search(ex,i)
        #if the pattern is fund in string
        if check:
            new_line = re.sub(ex,change,i)#use change function to substitute the match
            output.append(new_line)
        else:
            output.append(i)
    for _ in output:
        print(_)


#taking inputs
n = int(input("please enter the number of lines of string"))
lines = []
print("start entering lines")
for i in range(n):
    lines.append(input())

if len(lines)!= n:
    print("invalid input")
    sys.exit()

#calling teh function
substitution(lines)
