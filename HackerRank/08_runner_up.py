'''
Date - 04-08-2024
Author -  data-divaa
Question -
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given n scores.
Store them in a list and find the score of the runner-up.
'''

import sys
def runner_up(arr):
    #changing arr into list for easy opeartion
    arr_list = list(arr)
    score = []
    #elimanting duplicates
    for i in arr_list:
        if i not in score:#if ith element is avaiable no addition will happen
            score.append(i)
    #arranging score into ascending order
    for k in range(len(score)):
        for j in range(k+1):
            if score[k] < score[j]:
                #if condition comes true they switch place
                score[k],score[j] = score[j],score[k]
    #if there's only one element in score
    if len(score) == 1:
        print("there is no runner up")
        sys.exit()
        #if not as score is sorted into ascending the second last is our desirable result
    else:
        runner_score = score[-2]
        print(runner_score)


#taking inputs
print("----------intger only-----------")
n = int(input("enter the number of participate :"))
arr = map(int,input("enter the score score by participants : ").split())
if len(arr) != n:
    print("invalid input ........existing program")
    print("check if the number  score entered is same as number of participants ")
    sys.exit()


#caling function
runner_up(arr)
