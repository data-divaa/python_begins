'''
Date - 13 - October - 2024
Aurthur - Data-Divaa
Question -
you are given some phone number you have to decorative sort then in ascending order
'''

def fun(l):
    format = []
    for i in l:
        i = i[-10:]#takes up on last 10 digit of number
        format.append(f"+91 {i[:5]} {i[5:]}")
        #arranges it into the above order
    print("")
    print("after formatting:")
    for k in format:
        print(k)

n = int(input("enter the number of phone number:"))
l = [input() for _ in range(n)]

fun(l)
