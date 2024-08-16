lines= ['aas','sdasd']
n = 5
for i in lines:
    print(("-".join(i)).center((n+(n-1)+((n-1)*2)),"-"))
