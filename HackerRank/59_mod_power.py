'''
Date - 09 - September- 2024
Aurthur - Data-Divaa
Question - you are given three integer a,b,m.print
two lines
on the first line ,print the result of pow(a,b)
on the second line print the result of pow(a,b,m)
'''

a = int(input("enter the number:"))
b = int(input("enter the expotenial number who is to be raised to power:"))
m = int(input("enter the mod value:"))
print("after performing expotenet between",a,"and",b,"result is",pow(a,b))
print("after performing mod power :",pow(a,b,m))
