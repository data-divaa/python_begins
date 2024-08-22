'''
Date - 22 - august - 2024
Authur - Data - Divaa
Question -
    take two list make print their carestein product
'''


import itertools
#defining the function
def products(a,b):
    result = list(itertools.product(a,b))

    print(" ".join(f"({x[0]}, {x[1]})" for x in itertools.product(a,b)))
    #above line is just for desirable output
#taking inputs
a = list(input().split())
b =list(input().split())

#calling the function
products(a,b)
