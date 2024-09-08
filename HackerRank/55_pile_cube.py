'''
Date - 08 - September- 2024
Aurthur - Data-Divaa
Question -
there is a horizontal row of n cubes. the length of each cube is given. you need to create
a new vertical pile of cube . the new pile should follow these directions:if
cub[i] is on top of cube[j] then sidelength[j] >= sidelength[i].
when stacking the cubes. you can only pick either the leftmost or the rightmost
cube each time. print yess if it is possible to stack the cube otherwise print no
'''
from collections import deque

t = int(input("enter the number of test case:"))
result = []
for _ in range(t):
    n = int(input("enter the number of cubes:"))
    cubes = list(map(int,input().split()))
    cubes = deque(cubes)
    pile = []

    arrange_cube = sorted(cubes, reverse = True )
    if cubes[0] >= cubes[-1]:
        pile.append(cubes[0])
        cubes.popleft()
        for i in range(n-1):
            if (cubes[0] >= cubes[-1]) and (cubes[0] <= pile[-1]):
                pile.append(cubes[0])
                cubes.popleft()
            elif (cubes[0] < cubes[-1]) and (cubes[-1] <= pile[-1]):
                pile.append(cubes[-1])
                cubes.pop()
        if arrange_cube == pile:
            result.append("Yes")
        else:
            result.append("No")

    elif cubes[0] < cubes[-1]:
        pile.append(cubes[-1])
        cubes.pop()
        for i in range(n-1):
            if (cubes[0] >= cubes[-1]) and (cubes[0] <= pile[-1]):
                pile.append(cubes[0])
                cubes.popleft()
            elif (cubes[0] < cubes[-1]) and (cubes[-1] <= pile[-1]):
                pile.append(cubes[-1])
                cubes.pop()
        if arrange_cube == pile:
            result.append("Yes")
        else:
            result.append("No")



for i in result:
    print(i)
