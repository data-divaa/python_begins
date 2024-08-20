'''
Date - 20-july-2024
Authur - Data -Divaa
question -
Kevin and Stuart want to play the 'The Minion Game'.
--------------Game Rules-----------------
Both players are given the same string,S.
Both players have to make substrings using the letters of the string S
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
------------Scoring---------------------
A player gets +1 point for each occurrence of the substring in the string .S
---------------example---------------
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

print winner name and score separated by a space on one line,or draw if there is no winner
input will be the string to be counted
'''


import sys
#defining the function
def minion_game(string):
    vowel = ['A','I','E','O','U']#a list of vowels
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in vowel:
             kevin = kevin+(len(string)-i)
        else:
            stuart = stuart +(len(string)-i)

    '''
    The expression (len(string) - i) calculates the number of possible substrings that start
    at index i. For example, if the string is "BANANA" and i = 0 (the first 'B'),
    the substrings are BANANA, BANAN, BANA, BAN, BA, and B. This gives 6 possible substrings.
     If i = 1 (the first 'A'), the substrings are ANANA, ANAN, ANA, AN, and A, which gives 5
     possible substrings.
     So, (len(string) - i) gives the count of these substrings.
    '''
    if stuart >kevin:
        print("Stuart",stuart)
    elif stuart < kevin:
        print("Kevin",kevin)
    else:
        print("Draw")


#taking input
string = input("enter the word for the game(make sure to enter it in capitals)")
#input validation
for k in string :
    ascii_value = ord(k)
    if not( ascii_value < 90 and ascii_value >65):
        print("invalid input ........existing the program")
        sys.exit()


#calling the function
minion_game(string)
