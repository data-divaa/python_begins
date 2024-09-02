'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question - The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students
who have subscribed to both newspaper.
'''

import sys

def CountBoth(french,english):
    both = french & english#& is used as symbol for intersection
    print(len(both))

#taking inputs
nf = int(input("enter the number of student who read french newspaper: "))
f = list(map(int,input("enter the roll number of the students of those student (space seperated) ").split()))
#input validation
if len(f) != nf :
    print("invalid input....existing the program")
    sys.exit()
french = set(f)

ne = int(input("enter the number of student who read english newspaper: "))
e = list(map(int,input("enter the roll number of the students of those student (space seperated) ").split()))
#input validation
if len(e) != ne :
    print("invalid input....existing the program")
    sys.exit()
english = set(e)

CountBoth(french,english)
