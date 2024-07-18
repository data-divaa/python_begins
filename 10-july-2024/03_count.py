'''
Date - 12 - july - 2024
Author - Data-Divaa
Question -
Input a list from user, and input a number.
Count how many times that number occurs in the list and print it. Do not use any API
'''

#definig the function
def count(lst,num):
    #taking times as 0 so that when iteration found we can perform operation
    times = 0
    for i in lst: #we could have use range but here we did not because it will work just fine(don't mind it its for my understanding)
        if i == num:#if ith element of lst have the number to counted
            times = times + 1 # times will have 1 added to it
    return times


#taking input
lst = list(input("enter the list with space as seperator and make sure list elements are integer : ").split())
#in the above line we used string as the data type as it will have work with all of the data type as int asd float without any error
num = (input("enter thr number: ")

print(count(lst,num))
