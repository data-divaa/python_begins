'''
Date = 09 -july-2024
Authur = Data - Divaa
Question -
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

# definig teh function
def extension(filename):
    if '.' in filename:
        ind = filename.index('.') # here ind is storing the index of '.'
        ex = filename[ind+1:] # ex stores the string after '.' and +1 so that . can be removed to as
        return ex
    else:
        a = "invalid filename [make sure you are adding the file extension]"
        return a

# taking input
filename = input("please enter your filename : ")


#calling the function
print(extension(filename))
