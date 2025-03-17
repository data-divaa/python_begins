'''
author - Data - Divaa
Desc - a program to create a username with input taken name, birthyear,phonenumber, current year
'''

from itertools import product
import sys


#function to generate various combinations of lower and upper case character of the string
def password_generate(name):
    l1 = []
    for i in product(*[(ch.lower(),ch.upper()) for ch in name]):
        l1.append("".join(i))
    lst = l1.copy()
    return l1


#function to generate combinations with different symbols and birth year
def b_year_pw(l1,b_year):
    lst = []
    for i in l1:
        lst.append(i + "_" + b_year)
        lst.append(i + "-" + b_year)
        lst.append(i + "@" + b_year)
        lst.append(i + "#" + b_year)
        lst.append(i + "$" + b_year)
        lst.append(i + "!" + b_year)
        lst.append(i + "%" + b_year)
    return [k for k in lst]


#function to generate combinations with current year
def c_year_pw(l1,c_year):
    lst = []
    for i in l1:
        lst.append(i + "_" + c_year)
        lst.append(i + "-" + c_year)
        lst.append(i + "@" + c_year)
        lst.append(i + "#" + c_year)
        lst.append(i + "$" + c_year)
        lst.append(i + "!" + c_year)
        lst.append(i + "%" + c_year)
    return [k for k in lst]


#function to generate combinations with previous year
def p_year_pw(l1,p_year):
    lst = []
    for i in l1:
        lst.append(i + "_" + p_year)
        lst.append(i + "-" + p_year)
        lst.append(i + "@" + p_year)
        lst.append(i + "#" + p_year)
        lst.append(i + "$" + p_year)
        lst.append(i + "!" + p_year)
        lst.append(i + "%" + p_year)
    return [k for k in lst]


#function to generate combinations with mobile number
def m_num_pw(l1,m_num):
    lst = []
    for i in l1:
        lst.append(i + "_" + m_num)
        lst.append(i + "-" + m_num)
        lst.append(i + "@" + m_num)
        lst.append(i + "#" + m_num)
        lst.append(i + "$" + m_num)
        lst.append(i + "!" + m_num)
        lst.append(i + "%" + m_num)
    return [k for k in lst]


#taking input for password_genearte function
name = input("enter your name: ").strip()
if not name:
    print("NAME IS REQUIRED!!!")
    print("Existing the Program")
    sys.exit()
name_result = password_generate(name)

#copying the outputs from password_generate function for furthur use
final_result = name_result.copy()


#taking input for b_year_pw function
b_year = input("enter your birthyear(press enter to skip):").strip()
b_year = str(b_year)
if b_year and len(b_year) == 4 and b_year.isdigit():
    final_result.extend(b_year_pw(name_result,b_year))
elif b_year and (len(b_year) != 4 or not(b_year.isdigit())):
    print("INVALID INPUT EXISTING THE PROGRAM")
    sys.exit()


#taking input for c_year_pw function and p_year_pw function
c_year = input("enter the current year(press enter to skip):").strip()
if c_year and len(c_year) == 4 and c_year.isdigit():
    p_year = str(int(c_year) -1)
    c_year = str(c_year)
    final_result.extend(c_year_pw(name_result,c_year))
    final_result.extend(p_year_pw(name_result,p_year))
elif c_year and (len(c_year) != 4 or not(c_year.isdigit())):
    print("INVALID INPUT EXISTING THE PROGRAM")
    sys.exit()


#taking inputs for m_num_pw function
m_num = input("enter mobile number(press enter to skip):").strip()
m_num = str(m_num)
if m_num and len(m_num) == 10 and m_num.isdigit():
    final_result.extend(m_num_pw(name_result,m_num))
elif m_num and (len(m_num) != 10 or not(m_num.isdigit())):
    print("INVALID INPUT EXISTING THE PROGRAM")
    sys.exit()



#to print the final file with the output
with open("password_generate_output.txt", "w") as file:
    file.write("\n".join(final_result))

print(" Output file has been created with name - 'password_generate_output'")
