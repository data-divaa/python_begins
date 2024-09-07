'''
Date - 06 - September- 2024
Aurthur - Data-Divaa
Question - You are given n words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
'''

from collections import Counter

#defining function
def WordOrder(lst):
    record = Counter(lst)#to record the occurence and count in dictioanry form
    print(len(record.items()))
    xx = list(record.values())
    print(' '.join(map(str,xx)))


#taking input
n = int(input("enter the number of words:"))
lst = []
for _ in range(n):
    lst.append(input("enter the word:"))
    #function call
print("the deceasing order of occurence according to thier to count :")
WordOrder(lst)
