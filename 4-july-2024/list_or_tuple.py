"""
Date - 04 - july - 2024
Author - Data-Divaa
Question -

"""

# Definig function to generate a list
def generate_list(list1):
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i])
    return list2


# Definig function to generate a tupple
def generate_tuple(list1):
    tuple1 = tuple(list1)
    return tuple1


# taking input
print("enter your choice if one by one or in one go")
choice = input()

if choice == "one by one":
    # taking input for number of elements
    num = int(input("enter the number of elements in the data structure:  "))
    print("")
    list1 = []
    for k in range(num):
        element = input("enter the element:  ")
        if element.isdigit():
            list1.append(int(element))
        elif '.' in element:
            list1.append(float(element))
        else:
            list1.append(element)
else:
    # taking input for one go
    n = input("enter the data:   ")
    m = list(n)

    for j in range(len(m)-1,-1,-1):
        if m[j] == ',':
            m.pop(j)
    d = tuple(m)
# here when i one it work properply with string and float









if choice == "one by one":
    # calling function to generate list
    print(" with the given data list formed is:")
    print(generate_list(list1))
    print("")

    # calling function to generate tuple
    print("with given data tuple formed is :")
    print(generate_tuple(list1))
else:
    print(" with the given data list formed is:")
    print(m)
    print("")
    print("with given data tuple formed is :")
    print(d)
