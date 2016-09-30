#-*- coding: utf-8 -*-
'''
@author: birdlin
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver.get("http://portfolio.morningstar.com/Rtport/Reg/MyView.aspx?ViewPage=5#44-shownewsByDate")
assert "Morningstar" in driver.title

#driver = webdriver.PhantomJS(r'C:\Users\birdlin\AppData\Local\Programs\Python\Python35-32\phantomjs-2.1.1-windows\bin\phantomjs')
#driver.get("http://financials.morningstar.com/ratios/r.html?t=UA&region=USA&culture=en_US")
#assert "Morningstar" in driver.title

#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
#driver.switch_to_window(driver.window_handles[1])
#driver.get("http://www.python.org")

soup = BeautifulSoup(driver.page_source, 'lxml')
for title in soup.find_all('td'):
    for string in title.stripped_strings :
        print (string)

