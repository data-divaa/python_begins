'''
Date - 12- October - 2024
Aurthur - Data-Divaa
Question -
You are given a matrix of size N x M (rows and columns respectively).
You need to decode the matrix by reading column by column.
The goal is to extract only the alphanumeric characters (A-Z, a-z, 0-9) and concatenate them into a single string.
Any non-alphanumeric characters between alphanumeric characters should be replaced with a single space.
'''

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
#n stores the first digit entered

m = int(first_multiple_input[1])#and the second goes to m

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_string = ""
for col in range(m):
    for row in range(n):
        decoded_string += matrix[row][col]#helps to acceses each characters column by  colmhns

clean = re.sub(r'(?<=\w)(\W+)(?=\w)', ' ', decoded_string)
'''
we substitute the uncleaned string with the help of
regular expression
(?<\w) means lookbehind so that alphanumeric is proceeded by alphanumeric
(\w+) means one or more alphanumeric
(?=\w) means look ahead for aplhanumeric to be followed by alphanumeric
if not followed replace it by space""
'''
print(clean)
