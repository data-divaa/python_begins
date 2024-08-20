'''
Date - 20-july-2024
Authur - Data -Divaa
question -
You are given a string S and an integer k.
Your task is to divide the string S into n substrings,
each of length k. Then, for each substring, you need to remove
any duplicate characters while maintaining the order of the first occurrence
'''

import sys
#defining the function
def merge_tools(string,k):
    l1 = []
    xx = ""
    for i in range(0,len(string),k):#loop runs until string length withs steps as k
        x = string[i:i+k]#to ensure x contains substring of string with correct lenght
        for j in x:
            if j not in xx:
                xx = xx + j
        l1.append(xx)
        xx = ""#so that it stores new data
    for k in l1:
        print(k)

#calling the function
string = input("enter your string :")
k = int(input("enter the length of the substring: "))
if len(string) != k*k:
    print("invalid string and k pair ...existing the program")
    sys.exit()

#calling the function
merge_tools(string,k)
