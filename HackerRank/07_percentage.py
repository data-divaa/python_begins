'''
Date - 05 - august -2024
Author - Data-Divaa
question -
write code that  will read in a dictionary containing key/value
 pairs of name:[marks] for a list of students. Print the average
 of the marks arrayfor the student name provide,
  showing 2 places after the decimal.

input -
no. of students
data---name mark1 mark2
query_name

the final data form shouls be {"a":[10,20],"b":[40,90]}
'''


def percentage(student_marks,query_name):
    #by calling key name storing the value into varialbe query_marks
    query_marks = student_marks[query_name]
    #storing the number of marks inputted
    num_marks = len(query_marks)
    sum = 0
    for i in query_marks:
        sum = sum + i
    average = sum / num_marks
    #here format is used to so that wwe have two digits after decimal point
    average_round = format(average,".2f")
    return average_round


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(percentage(student_marks,query_name))
