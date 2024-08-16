'''
Date - 13 - august - 2024
Authur - Data - Divaa
Question -
    Given an integer, , print the following values for each integer from to:
    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary
'''


def conversion(n):
    w = len(bin(n)[2:])
    for i in range(1,n+1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(dec.rjust(w),octa.rjust(w),hexa.rjust(w),bina.rjust(w))


n = int(input())

conversion(n)
