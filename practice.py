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
