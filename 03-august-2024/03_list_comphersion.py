'''
Authur - Data - Divaa
Date - 03 - august- 2024
Question-
        input four integer x,y,z,n where x,y,z are 3d coordinates[x,y,z] and
x+y+z != n
for example -
 x = 2
 y = 2
 z = 2
 n = 2
 then output should be

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2]
, [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
[1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
 [2, 2, 0], [2, 2, 1], [2, 2, 2]]

'''


#definning the function
def list_comphersion(x,y,z,n):
    '''
    here list comphersion is used where basically instead of nested loop
    where all required loop and steps are taken in a list .
    Here, i needed nested in i,j,k format so the code
    and i had to equal to or less than x and same goes for other j and k element
    with the help of for loop element form the list
    and if the condition if satisfied it gets added to the main list coordinate which is our main list
    '''
    coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    return coordinates

#taking inputs
x = int(input("enter the first number "))
y = int(input("enter the second number "))
z = int(input("enter the third number "))
n = int(input("enter the  number  whose summ is not expected "))

#calling function
print("the 3D coordinate of ",x,y,z," whose sum is not equal to ",n,"is ")
print(list_comphersion(x,y,z,n))
