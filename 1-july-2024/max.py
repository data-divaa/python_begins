# to get the maximum out of a list manually
def maximum_manually(li):
	com = 0
	for i in li:
		if com < i :
			com = i
	return com

	
# calling maximum_manualy function
li = [23,43,787,75665,1,65746,777]
 maximum_manually(li)

 # to get the maximum out of a list through input
 list1 = []
 for i in range(10):
 	num1 = int(input("enter number:"))
 	list1.append(num1)
 print("The list formed  with the given input is:  ")
 print("list1")
 maxi = 0
 for k in list1:
 	if maxi < k:
 		maxi = k
 print(maxi)


 # to get the minimum out  of a list manually
 def minimum_manually(list2):
 	compare = list2[0]
 	for s in list2:
 		if compare > s:
 			compare = s 
 	return compare

#calling minimum function
 minimum_manually([565,2342,546345,222,787776,34,1,34,2313])


#to get the input for minimum 
list3 =[]
for d in range(10):
	num2 = int(input("enter a numer"))
	list3.append(num2)
print("The list formed  with the given input is:  ")
 print(list3)
 a = list3[0]
 for o in list3:
 	if a> o :
 		a = o
print(a) 


#reversing my name
def reversing_myname(name):
	rev=0
	for i in range(len(name)-1,-1,-1):
		rev_name = rev + i
	return rev_name


#calling reverse name main function
reversing_myname(pihu)


# removing the fifth charcter of a string
def remove_fifth(stri):
	a = 4
	p = ""
	for i in range(len(stri)):
		if a != i:
			p = p + stri[i]
	return p
			
remove_fifth("hermione")
