'''
Date - 09 - September- 2024
Aurthur - Data-Divaa
Question - we have print the average of students marks obtained in all the subject
'''



#defining the function
def avg_std(marks):
    #we use * to take all the list present in marks
    std_mark = list(zip(*marks))
    for i in std_mark:
        sum = 0
        for j in i:
            sum = sum + j
        std_avg = sum / len(i)
        print(std_avg)


#taking inputs
num_std,num_sub = map(int,input().split())
marks = []
for _ in range(num_sub):
    marks.append(list(map(float,input().split())))

#calling function
avg_std(marks)
