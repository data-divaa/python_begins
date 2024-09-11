'''
Date - 11 - September- 2024
Aurthur - Data-Divaa
Question -
Your task is to sort the string in the following manner
-All sorted lowercase letters are ahead of uppercase letters.
-All sorted uppercase letters are ahead of digits.
-All sorted odd digits are ahead of sorted even digits.
'''

string = input()
lowercase = sorted([i for i in string if i.islower()])
uppercase = sorted([i for i in string if i.isupper()])
odd = sorted([i for i in string if i.isdigit() if int(i) %2 != 0])
even =sorted([i for i in string if i.isdigit() if int(i) %2 == 0])
print("-All sorted lowercase letters are ahead of uppercase letters.")
print("All sorted uppercase letters are ahead of digits.")
print("-All sorted odd digits are ahead of sorted even digits.")
print(''.join(lowercase+uppercase+odd+even))

'''
we take a string then we seperatly sort lower,upper ,odd and even and then just add all the list
together to print the elements as string with the help of join
'''
