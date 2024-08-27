'''
Date - 27- august- 2024
Aurthur - Data-Divaa
Question -
you will be given 2 integer n and m . there are n words which
might repet in word group A. there are m words
belonging to word group b for each m words check
whether the word has apperaed in group a or not.
print thr indicies of each occurence of m in group A.
if it does not appear print -1
'''
from collections import defaultdict

#defining the function
def defaultdict_function(a,b):
    dict = defaultdict()
    for i in b:
        if i in a:
            dict[i]= [y + 1 for y, x in enumerate(a) if x == i]
            #here we add 1 to the indicies as per desirable output also we use enumertae for the indicies of the values
            print(' '.join(map(str,dict[i])))
            #now as per output we join the value of the key at i and print it
        else:
            print(-1)
            #if the key is not present print -1

#taking input
n,m = list(map(int,(input("enetr the number of elements is group a and group b respectively space as seperator ").split())))
a = []
b = []

print("enter the values of group a after eachvalue press enter")
for k in range(n):
    a.append(input())
print("enter the values of group a after eachvalue press enter")
for j in range(m):
    b.append(input())

#calling the function
print("the indicies where the elements of group b are present in group a are..")
defaultdict_function(a,b)
