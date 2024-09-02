'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question -
there is an array of n integers.there are also disjoint sets
A and B , each containing m integers . you like alll the integer
in set A and dislike all the intger in set B.your initial happiness is 0
for each i integer in the array, if i belongs to A you add
1 to your happiness if i belongs to B you add -1
to your happiness other your happiness stayes the same

Note: Since A and B are sets, they have no repeated elements. However,
the array might contain duplicate elements.
'''



import sys



#defining the function
def happiness_counter(a,b,nlist):
    happiness = 0
    '''
    we run a loop through nlist if the element is in a we add 1
    if not -1 else leave it
    '''
    for i in nlist:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
        else:
            pass
    return happiness

#taking the inputs
n,m = map(int,input("enter the number of elements in array and sets respectively space seperated: ").split())

nlist = list(map(int,input("enter the array space seperated: ").split()))
#input validation
if len(nlist) != n:
    print("invalid input....existing the program")
    sys.exit()


a = set(map(int,input("enter the elements of set A space seperated: ").split()))
#input validation
if (len(a) != m):
    print("invalid input....existing the program")
    sys.exit()

b = set(map(int,input("enter the elements of set A space seperated:").split()))
#input vaidation
if (len(b) != m):
    print("invalid input....existing the program")
    sys.exit()


#calling the function
print(happiness_counter(a,b,nlist))
