'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
Input a list from user, and input a number.
Count how many times that number occurs in the list and print it. Do not use any API
'''
import sys
#defining the function
def count(lst,num):
    # times is taken as 0 for furthur use
    times = 0
    for i in lst:
        if i == num:#if i is equal to num
            times = times + 1 # 1 addes to times for count
    return times


#taking inputs
lst = list(input("enter the list(make sure it containes integer) separted by space").split())
#input validation
for k in lst:
    ascii_value = ord(k)#each element of lst is changed into its ascii value
    if not(48 <= ascii_value <= 57):# if the ascii_value exceeds the parameters following steps are taken
        print("invalid integer ... existing the program")
        sys.exit()#if the if statement comes true program is exited
print("list entered :",lst)

num = input("enter the number to be counted : ")
#input validation
value = ord(num)# the num is also changed ascii
if not (48 <= value <= 57):
    print("invalid number .... exiting the program")
    sys.exit()

#calling function
print("number of times ",num,"appeared in the list is ",count(lst,num))
