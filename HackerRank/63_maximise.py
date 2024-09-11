'''
Date - 10- September- 2024
Aurthur - Data-Divaa
Question -
there is a f(x) = x**2 and we have to find the maximum of f(x1)+f(x2)......+f(xk)%m
where x1 is an element of one list, x2 of second anf xk of k list
here we have to take input of number list and their modulus and their elemnts of list
'''

from itertools import product

k,m = map(int,input("enter the number of indeices and modulus space seperated:").split())
lst = []
for _ in range(k):
     lst.append(list(map(int,input().split()[1:])))
     #here we store inputted list from index 1 because that is want we actually need

comb = list(product(*lst))#with the help of * we use all the lst stored in lst
result = []
for tuple in comb:
    total = 0
    #we run a loop on the tuples present in combination formed and then again on the elements of the tuples
    #we take each element and sqaure it and then add it  after doing modulus also storing it i result

    for i in tuple:
        total += pow(i,2)
    result.append(total%m)
#finally printing the maximum out of the list


print("maximum output from the function is :",max(result))
