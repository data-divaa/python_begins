'''
Date - 11 - September- 2024
Aurthur - Data-Divaa
Question -
You are given a space separated list of integers.
If all the integers are positive,
then you need to check if any integer is a palindromic integer.
'''

n = int(input("enter the number of list:"))
lst = list(map(int,input("enter the list:").split()))
result = (all(i>0 for i in lst)) and (any(str(k)==str(k)[::-1] for k in lst))
'''
if all the elements are positive that is greater than 0 and if any one of them is
palindrone
'''
print("True will be printed if if all the elements are positive that is greater than 0 and if any one of them is palindrone otherwise false")

print("the result is ",result)
