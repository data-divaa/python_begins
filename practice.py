import itertools
num = [1,1,2,2,2,4,4,3,3,3,3]
group = itertools.groupby(num)
l = [(len(list(grouped)),key) for key,grouped in group]
print(' '.join([f"({key}, {count})"for key,count in l]))
