'''
Date - 06 - September- 2024
Aurthur - Data-Divaa
Question -
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string
, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

    -Print the three most common characters along with their occurrence count.
    -Sort in descending order of occurrence count.
    -If the occurrence count is the same, sort the characters in alphabetical order.

'''
from collections import Counter
import sys
s = input()
s = list(s)
count_counter = Counter(s)#form a dictionary of count and key
order = sorted(count_counter.items(),key=lambda x:(-x[1],x[0]))
'''
now we sort the items first on the basis of value but we add -x[1]
so that each one became negative like 10 will become -10 so when arrange ascending it will lies at first
and is desirable for our output now if the values are multiple we sort into ascending order according # TODO: their key with x[0]
'''
top_three= order[:3]#take up on the top three
for x,y in top_three:
    print(f"{x} {y}")
