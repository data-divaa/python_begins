'''
Date - 26- august- 2024
Aurthur - Data-Divaa
Question - take input a list of numbers and print the average of the distinct numbers
'''
#defining the function
def average(arr):
    sum = 0
    distinct_values = set(arr)#using sets for unique values
    l = len(distinct_values)
    for i in distinct_values:
        sum = sum + i
    output = sum / l
    format_output = "{:.3f}".format(output)#for three decimal
    return format_output

#taking input
n = int(input("enter the number of data to be entered"))
arr = list(map(int,input("enter the data space seperated").split()))
#calling the function
print("average of unique values upto three decimal is:")
print(average(arr))
