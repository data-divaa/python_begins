'''
Date - 08 - September- 2024
Aurthur - Data-Divaa
Question - take input n and print a numerical triangle of height n-1
like this ---
1
22
333
44444
........
'''

for i in range(1,int(input())):
    print(((10 ** i)// 9)*i)
'''
here
1 = 1 *1
22 = 11* 2
333 = 111*3
.......
'''
