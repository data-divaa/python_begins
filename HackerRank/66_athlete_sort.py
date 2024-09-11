'''
Date - 11 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a spreadsheet that contain a list of # NOTE: athletes
and their details(such as age, height,weight and so on). You
are required to sort the data based on the kth attribute and print
the final resulting tables.
'''

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
k = int(input())


sort_arr = sorted(arr,key = lambda x:x[k])

for i in sort_arr:
    print(' '.join(map(str,i)))
