'''
Date - 17 - September- 2024
Aurthur - Data-Divaa
Question -
you are given string s and it consist of alphanumeric character spaces and symbols(+-)
your task is to find all the substring of s that contains 2 or more vowels.
also these substring must lie in between 2 consonanat and should conatain vowels only
'''

import re

def find_vowel(string):
    ex = r"(?=[^aieouAIEOU]([aieouAIEOU]{2,})[^aieouAIEOU])"
#pattern says that check ahead if 2 or more vowels are surrounded by non-vowels without including the non-vowels
    result = re.findall(ex,string)#now findall that matches with the pattern and string
    if result:

        return '\n'.join(result)
    else:
        return -1

#taking inputs
string = input("enter the string to check for vowels (2 or more) surrounded by non-vowels:")

#calling function
print("the vowels found satisfying the condition are:")
print(find_vowel(string))
