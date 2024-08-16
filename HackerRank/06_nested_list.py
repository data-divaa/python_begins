'''
Date - 04-08-2024
Author -  data-divaa
Question -
Given the names and grades for each student in a class of students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.

input -[["chi",20.0],["beta",50.0],["aplha",50.0]]
output - aplha
        beta

Note - take input in each line first name and then in different line marks
for example - harry
            23.56
            jojo
            43.5
'''

def second_lowest(record):
    n = len(record)#storing length of records
    for k in range(n):#loop runs for total elements
        for j in range(0,n-k-1):
            if record[j][1] > record[j+1][1]:#through indexing record is arranged in ascending from
                record[j],record[j+1] = record[j+1],record[j]#arrangement in order
    no_dulpicate = []
    #chnage to set
    for t in record:
    #if the 2nd element of nested list is not in no_dulpicate then only the the seconde element is extracted and putted inside no_dulpicate
        if t[1] not in [x[1] for x in no_dulpicate]:
            no_dulpicate.append(t)

    second_lowest_score = no_dulpicate[1][1]
    asc_name = []
    for f in record:
        if f[1] == second_lowest_score:#through index number verified
            asc_name.append(f[0])
    asc_name.sort()
    for l in asc_name:
        print(l)

num = int(input("enter the number of students whose data is to fed "))
record = []
data = []
for i in range(num):
    name = input("enter the name of student : ")
    score = float(input("enter the number of the student "))
    data.append(name)
    data.append(score)
    record.append(data)
    data = []



second_lowest(record)
