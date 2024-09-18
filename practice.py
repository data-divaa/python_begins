iimport re

def change(s):
    if s.group() == " && ":
        return " and "
    elif s.group() == " || ":
        return " or "
    else :
        return s.group()

def substitution(lines):
    ex = r"\s&&\s|\s\|\|\s"
    output= []
    for i in lines:
        check = re.search(ex,i)
        if check:
            new_line = re.sub(ex,change,i)
            output.append(new_line)
        else:
            output.append(i)
    for _ in output:
        print(_)



n = int(input())
lines = []
for i in range(n):
    lines.append(input())


substitution(lines)
