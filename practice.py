'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question - The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students
who have subscribed to at least one newspaper.
'''

def CountAtleastOne(french,english):
    union_set = french | english'''
    Date - 02 - September- 2024
    Aurthur - Data-Divaa
    Question - The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
    You are given two sets of student roll numbers.
    One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students
    who have subscribed to at least one newspaper.
    '''

    def CountAtleastOne(french,english):
        union_set = french | english
        for i in english:
            if (i not in union_set) :
                union_set.add(i)
        for j in french:
            if (j not in union_set):
                union_set.add(j)
        print(len(union_set))

    nf = int(input("enter the number of students who read french newspaper:"))
    f = list(map(int,input("enter the roll number those student who read french newspaper(space seperated) ").split()))
    if len(f) != nf:
        print("invalid input.....existing the program")
        sys.exit()
    french = set(f)

    ne = int(input())
    e = list(map(int,input().split()))
    if len(e) != ne:
        print("invalid input.....existing the program")
        sys.exit()
    english = set(e)

    CountAtleastOne(french,english)

    print(len(union_set))

nf = int(input("enter the number of students who read french newspaper:"))
f = list(map(int,input("enter the roll number those student who read french newspaper(space seperated) ").split()))
if len(f) != nf:
    print("invalid input.....existing the program")
    sys.exit()
french = set(f)

ne = int(input())
e = list(map(int,input().split()))
if len(e) != ne:
    print("invalid input.....existing the program")
    sys.exit()
english = set(e)

CountAtleastOne(french,english)
