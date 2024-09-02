'''
Date - 02 - September- 2024
Aurthur - Data-Divaa
Question -
given 2 sets of integers, M and N,print their symmetric is ascending
order.
'''

#defining the function
def symm_diff(m_set,n_set):
    lst = sorted(m_set ^ n_set)
    for _ in lst:
        print(_)

#taking input
m = int(input("enter the number of elements in set M:"))
m_list = list(map(int,input("enter the set elements space seperated").split()))
m_set = set(m_list)
n = int(input("enter the number of elements in set N:"))
n_list = list(map(int,input("enter the set elements space seperated:").split()))
n_set = set(n_list)

#calling the function
print("after applying the symmteric differnce the elements of set formed is:")
symm_diff(m_set,n_set)
