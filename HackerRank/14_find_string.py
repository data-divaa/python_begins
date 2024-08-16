'''
Date - 08 - august - 2024
Authur - Data - Divaa
Question -
    a string is given and a substring is given define a function to count and print
    how many times has the substring appears in the main string

    string traversal will take place from left to right..
    NOTE - string are case sensitive
'''

def count_substring(string,substring):
    count = 0
    for i in range(len(string)-len(substring)+1):
        '''
    #this range is so to check each and every possible occurence
    #here for exampe if string is of 8 character and substring is of 2
    #then for fair check the range must go up to the last i.e 7 hence adding 1
    #also len(substring) is subtracted to avoid index error'''
        if string[i:i+len(substring)] == substring:

            '''
            through slicing if from ith position to ith + the len of subtring
            matches with substring inpuuted then true
            and count adds 1
            '''
            count += 1
    return count


string = input("enter the string which needs to be checked for repeatation of substring :")
substring = input("enter the string whose appearace needs to be checked in the main string :")

print(count_substring(string,subtring))
