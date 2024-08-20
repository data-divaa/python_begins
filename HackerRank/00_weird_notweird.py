'''
Date - 8-july-2024
Authur - Data -Divaa
question -
Given an integr n perform the following conditional actions:
If n is odd print Weird
If n is even and in inclusive range of 2 to 5 print Not Weird
If n is even and in the inclusive range 6 to 20 print Weird
If n is even and greater than 20 print Not weird
'''


def weird_notweird(n):
    if n % 2 != 0:
        print("Weird")
    elif (n % 2 == 0) and (n>= 2 and n<= 5):
        print("Not Weird")
    elif (n % 2 == 0) and ( n >=6 and n<= 20):
        print("Weird")
    else:
        print("Not Weird")

#taking inputs
n = int(input("enter the number to check if even or odd :"))



weird_notweird(n)



a = input()
aa =a.split()
if aa[0][0].islower():
    for i in aa:
