#-*- coding: utf-8 -*-
'''
@author: birdlin
'''
import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from openpyxl import Workbook
from builtins import int

#wb = Workbook()
#ws = wb.active
'''
url = 'http://financials.morningstar.com/ratios/r.html?t=UA&region=usa&culture=en-US'
#list = []
with urlopen(url) as response:
    soup = BeautifulSoup(response.read(), 'lxml')

#for th in (soup.find_all('thead')):
print (soup.find_all('script'))
'''
url = 'http://dcsd.nutrislice.com/menu/meadow-view/lunch/'

with urlopen(url) as text:
    p = re.compile(r'bootstrapData', text)
    menu = json.loads(p.string)
    print (menu)

'''
text = urlopen('http://dcsd.nutrislice.com/menu/meadow-view/lunch/').read()
menu = json.loads(re.search(r"bootstrapData\['menuMonthWeeks'\]\s*=\s*(.*);", text).group(1))
'''
#print (text)


'''
for tag in (soup.select("tbody:nth-of-type(1)")):
    for number in tag.find_all('td', class_ = re.compile(r'12')) :
        for string in number.stripped_strings :
            ws.cell(row=row_index, column=column_index).value=string
            column_index += 1
            if column_index > 15 :
                row_index += 1
                column_index = 1
'''

