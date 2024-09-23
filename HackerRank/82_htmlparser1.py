'''
Date - 23 - September- 2024
Aurthur - Data-Divaa
Question -
you are given a python code using html parser divide into start,end and empty tags also attributes and their value
use -> for attributes and > for their value
'''


from html.parser import HTMLParser

class myHTMLParser(HTMLParser):#creating class where HTMLParser's function can work
#here we could have used a differenct class name but parameter has to be HTMLParser
    def handle_starttag(self, tag, attrs):
        #using the handle_starttag to find the start tag of html
        print(f"Start : {tag}")
        for i in attrs:#if it attributes then [0] = atttribute name [1] gives value
            print(f"-> {i[0]} > {i[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")
#endtag and startend follow the same logic but since end do not have any attritubute we do nt need to use atttribute
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")


html_data = ''
n = int(input("enter the number of lines in HTML code:"))
print("-----------just enter the code ------------")
for i in range(n):
    html_data += input().strip() + '\n'
#here we have created a empty string were we are going to add all the string if space occured


parser = myHTMLParser()
parser.feed(html_data)#feeding the data stored in html_data into the class which is stored parser
