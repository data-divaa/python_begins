'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
Input a list from user, and input a number.
Count how many times that number occurs in the list and print it. Do not use any API
'''


def count(lst,num):
    times = 0
    for i in range(len(lst)):
        if lst[i] == num:
            times = times + 1
    return times

lst = list(map(int,input("enter the list with commas as seperator: ").split(',')))
num = int(input("enter thr number: "))

print(count(lst,num))
