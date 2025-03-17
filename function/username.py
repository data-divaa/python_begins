'''
aurthur - Data - Divaa
topic - a program to create a username with input taken name, birthyear,phonenumber, current year
'''

import sys
from itertools import product

def usernames(name):
    l1 = []
    for i in product(*[(ch.lower(),ch.upper()) for ch in name]):
        l1.append("".join(i))

    lst = l1.copy()

    b_year = int(input("enter your birthyear :"))
    b_year = str(b_year)
    for i in l1:
        lst.append(i + "_" + b_year)
        lst.append(i + "-" + b_year)
        lst.append(i + "@" + b_year)
        lst.append(i + "#" + b_year)
        lst.append(i + "$" + b_year)
        lst.append(i + "!" + b_year)
        lst.append(i + "%" + b_year)


    c_year = int(input("enter the current year :"))
    p_year = c_year - 1
    c_year = str(c_year)
    if len(c_year) == 4:
        for i in l1:
            lst.append(i + "_" + c_year)
            lst.append(i + "-" + c_year)
            lst.append(i + "@" + c_year)
            lst.append(i + "#" + c_year)
            lst.append(i + "$" + c_year)
            lst.append(i + "!" + c_year)
            lst.append(i + "%" + c_year)


    p_year = str(p_year)
    for i in l1:
        lst.append(i + "_" + p_year)
        lst.append(i + "-" + p_year)
        lst.append(i + "@" + p_year)
        lst.append(i + "#" + p_year)
        lst.append(i + "$" + p_year)
        lst.append(i + "!" + p_year)
        lst.append(i + "%" + p_year)


    m_num = int(input("enter mobile number:"))
    m_num = str(m_num)
    if len(m_num) == 10:
        for i in l1:
            lst.append(i + "_" + m_num)
            lst.append(i + "-" + m_num)
            lst.append(i + "@" + m_num)
            lst.append(i + "#" + m_num)
            lst.append(i + "$" + m_num)
            lst.append(i + "!" + m_num)
            lst.append(i + "%" + m_num)
    else:
        sys.exit()

    set1 = set(lst)
    return len(set1)



name = input("enter your name :")
result = usernames(name)
print(result)

#with open("usernames_output.txt", "w") as file:
    #file.write("\n".join(result))
