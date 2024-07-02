'''
Date - 1-07-2024
Author -  data-divaa
Question ------------------------------------------------
	-
	-
	-
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
	rev=0
	for i in range(len(name)-1,-1,-1):
		rev_name = rev + i
	return rev_name

# removing the fifth charcter of a string
def remove_fifth(stri):
	a = 4
	p = ""
	for i in range(len(stri)):
		if a != i:
			p = p + stri[i]
	return p


# Input the list
#----------------------------------------add the list size also as input
list1 = []
for i in range(10):
	num1 = int(input("enter number:"))
	list1.append(num1)
print("The list formed  with the given input is:  ")

# calling maximum_manualy function
print("maximum of the list is ", maximum_manually(list1))


#calling minimum function
print("minumum of the list is ", minimum_manually(list1))


#---------------------------------------make a user input for both below, then use print statement to print it.

#calling reverse name main function
#reversing_myname("pihu")

# removing character
#remove_fifth("hermione")
