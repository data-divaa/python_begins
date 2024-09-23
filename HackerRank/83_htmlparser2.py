'''
Date - 23 - September- 2024
Aurthur - Data-Divaa
Question -
you are given html code and your task is to print is
to print single - line comment , multiple - line comment and data
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self,data):
        if data.strip():
            print(">>> Data")
            print(data)



html = ""
for i in range(int(input("enter the number of lines of code for html "))):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
