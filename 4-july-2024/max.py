'''
Date - 1-07-2024
Author -  data-divaa
Question -
		1. maximum out of a list
		2. minimum out of a list
		3. reverse the nane
		4. removing fifth character
'''

# to get the maximum out of a list manually
def maximum_manually(li):
	com = 0
	for i in li:
		if com < i :
			com = i
	return com

# to get the minimum out  of a list manually
def minimum_manually(list2):
	compare = list2[0]
	for s in list2:
		if compare > s:
			compare = s
	return compare

#reversing my name
def reversing_myname(name):
	rev=""
	for i in range(len(name)-1,-1,-1):
		rev = rev + name[i]
	return rev

# removing the fifth charcter of a string

def remove_fifth(stri):
	p = ""
	for i in range(len(stri)):
		if char != i:
			p = p + stri[i]
	return p


# # Input the list
# list1 = []
# size = int(input("enter the number of elements you would like to have in the list:   "))
# for i in range(size):
# 	num1 = int(input("enter number:"))
# 	list1.append(num1)
# print("The list formed  with the given input is:  ")
#
# # calling maximum_manualy function
# print("maximum of the list is ", maximum_manually(list1))
#
#
# #calling minimum function
# print("minumum of the list is ", minimum_manually(list1))
#
#
# name = input("enter the name to be reversed :    ")
#
# #calling reverse name main function
# print("reversed given name : ", reversing_myname(name))
#
# # removing character
# char = int(input("enter thr index to be removed"))
# str1 = input("enter the string whose character is to be removed:"   )
# print("after the removal of", char,"character string looks like this",remove_fifth(str1))
