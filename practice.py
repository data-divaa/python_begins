import re
ex = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
s = input()
if re.search(ex,s):
    print("valid email")
else:
    print("not valid email")
