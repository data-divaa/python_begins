'''
Date - 25 - july - 2024
Author - Data-Divaa
Question -
3. Write a Python program to check whether the given strings are
palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]

'''

#defining the function
def palindrome(string_list):
    result = []#empty list for furthut opeartions
    for i in string_list:
        a = ""
        for k in range(len(i)-1,-1,-1):#this loop changes each element of the list into reverse
            a = a + i[k]#then stores it in a string
        if a == i:#if the reverse and original are same
            result.append("True")#result have a true
        else:# if not then false
            result.append("False")
    return result


#taking input
print(" ")
string_list = list(input("ENTER THE LIST  WITH SPACE AS SEPERATOR WHICH IS TO CHECK IF THEY ARE PALINDROME :").split())
print("ENTERED LIST : ",string_list)
print(" ")

#calling function
print("IF THE LIST ELEMENT IS TRUE THEN IT THE STRING ENTERED IS PALINDROME AND IF NOT THEN FALSE ")
print(palindrome(string_list))
