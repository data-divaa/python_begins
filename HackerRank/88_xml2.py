'''
Date - 25 - September- 2024
Aurthur - Data-Divaa
Question -
given a valid XML document you have to print the maximum level
of nesting in it take the depth of the root as 0
'''


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1#increment as we go deeper
    if level > maxdepth:
        maxdepth = level #update if current levelmis high

    for child in elem:#following recursive call until leaf node found
        depth(child, level)



if __name__ == '__main__':
    n = int(input("enter the number of lines xml file contain"))
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))#used to change the text into element object
    depth(tree.getroot(), -1)#get the root elements
    print(maxdepth)
