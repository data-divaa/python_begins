'''
Date - 13 - august - 2024
Authur - Data - Divaa
Question -
    you are given an integr N your task is to print an aplhbet rangoli of size N
'''
import sys

#defining the function
def rangoli(n):
    #taking alphabets in a string but can also use ascii value
    alp = "abcdefghijklmnopqrstuvwxyz"
    zz = []
    oo = []
    for i in range(n-1,-1,-1):
        #range goes in reverse order
        #through indexing value s stored in xx
        xx = alp[i]
        if i == n-1:
            #for first that is n-1
            zz.append(xx)#added to an empty list
            oo.append(zz.copy())#copy that to a new list
        elif i == n-2:#for second element addition
            zz.append(xx)#first add the alphabet
            zz.append(zz[0])#then add the previously existing elemnt
            oo.append(zz.copy())#again copy to oo list for futhur use
        else:
            l = len(zz)#storing the length of oo in l for ease
            del zz[(l//2)+1:]#deleting the values from zz that are repeated
            zz.append(xx)#now new value is added
            rr = zz[0:-1][::-1]#then the elements prsent in zz before the addition of new element is reversed
            zz.extend(rr)#then added to zz through extent so that it does not form a nested list
            oo.append(zz.copy())#copy that to oo as elements

    for k,h in zip(range(n),oo):
        print(("-".join(h)).center((n+(n-1)+((n-1)*2)),"-"))
#here we join the nested element of oo through - for desirable length

    oo.pop()#removed the last from oo since we do not need it
    for p,q in zip(range(n-1),range(len(oo)-1,-1,-1)):#same logic as before just reversed
        print(("-".join(oo[q])).center((n+(n-1)+((n-1)*2)),"-"))




#taking inputs
n = int(input("enter the number for alphabet rangoli as (1 for a)(2 for b)...(26 for z): "))
if not (n>1 and n<27):
    print("invalid input ....existing the program")
    sys.exit()

#calling the function
rangoli(n)
