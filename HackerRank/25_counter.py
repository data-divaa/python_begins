'''
Date - 22 - august - 2024
Authur - Data - Divaa
Question -
raghav is a shoe shop owner. His shop has number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay

amount of money only if they get the shoe of their desired size.

Your task is to compute how much money raghav earned.

'''
from collections import Counter

#defining the function
def shoe_shop(xx):
    count = Counter(xx)#forming a dictionary of shoe zie and number of shoes
    money = 0
    for k in l1:
        if k[0] in count.keys():#if shoe size aviable in in keys
            money = money + k[1]#add the price of corresponding to money
            count[k[0]] -= 1#and subtract 1 from the value of the key of the show size
            if count[k[0]] == 0:#if the value of a key becomes zero delete the key avlue pair
                del count[k[0]]

        else:
            pass
    print(money)

#taking inputs
x = int(input("enter the number of shoes: "))
xx = list(map(int,input("enter the sizes avaialbe of shoes in the shop:").split()))
n = int(input("enter the number of customers : "))
l1 = []
for i in range(n):
    sp = list(map(int,input("enetr the size of shoe and price: ").split()))
    l1.append(sp)


#calling the function
shoe_shop(xx)
