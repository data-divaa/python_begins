'''
Date - 03 - july -2024
Author - Data-Divaa
question - arranging the list into ascending and descending order
'''


# defining function for ascending order sorting of a list
def arrange_asecnding(your_list):
    for i in range(len(your_list)):
        for k in range(i+1):
            if your_list[i] < your_list[k]:
                your_list[i] , your_list[k] = your_list[k] , your_list[i]
    return your_list


# defining function for descending order sorting of a list
def arrange_descending(your_list):
    for a in range(len(your_list)):
        for b in range(a+1):
            if your_list[a] > your_list[b] :
                your_list[a] ,  your_list[b] = your_list[a] , your_list[b]
    return your_list


#taking input for numbers of element
num = int(input("enter the number of elements you would like to have in the list----"))
print("")

# taking input for numbers in the your_name list
your_list = []
for j in range(num):
    numb = int(input("enter the number-----"))
    your_list.append(numb)
print("list formed with given inputs:")
print(your_list)
print("")


# calling the main function for ascending order
print("obtained list in ascending form:")
print(arrange_asecnding(your_list))
print("")


#  calling the main function for descending order
print("obtained list in descending form:")
print(arrange_descending(your_list))
