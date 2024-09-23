'''
Date - 23 - September- 2024
Aurthur - Data-Divaa
Question -
you are task is to detect and print all the html tags , attributes and their values
'''

from html.parser import HTMLParser

class myHTMLparser(HTMLParser):

# here we only use starttag and startend because only these both take attributes
    def handle_starttag(self,tag,attrs):
        print(tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

    def handle_startendtag(self,tag,attrs):
        print(tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")



html_data = ''
for i in range(int(input("enter the number of line sof code for html code"))):
    html_data += input().strip()


parser = myHTMLparser()
parser.feed(html_data)
