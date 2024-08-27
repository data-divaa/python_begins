'''
Date - 27- august- 2024
Aurthur - Data-Divaa
Question - print the error if occurede betwen valueerror or zeroerror
'''
'''
Date - 27- august- 2024
Aurthur - Data-Divaa
Question - take 2 input and do their integer division if any error print the error
'''

def error(x):
    for k in x:
        #try and except is usually used for error
        try:#print it until a error occurs
            print(int(k[0])//int(k[1]))#we use indexing for proper division as they both are in a list
        except ZeroDivisionError as ze:# when zero error ocur stored it in ze
            print("error code:",ze)#and then print
        except ValueError as ve:#same logic as above
            print("error code:",ve)


#taking the input
n = int(input("enter the number of test cases to be performed :"))
x = []
for i in range(n):
    xx = list(input().split())
    x.append(xx)

#calling the function
error(x)
