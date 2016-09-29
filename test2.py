#-*- coding: utf-8 -*-
'''
@author: birdlin
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver = webdriver.PhantomJS(r'C:\Users\birdlin\AppData\Local\Programs\Python\Python35-32\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://financials.morningstar.com/ratios/r.html?t=UA&region=USA&culture=en_US")
#driver.get("http://www.python.org")
assert "Morningstar" in driver.title
soup = BeautifulSoup(driver.page_source, 'lxml')
for title in soup.find_all('td'):
    print (title)

driver.quit()


''' 
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver.get("http://www.google.com.tw")
#driver.get("http://www.python.org")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
print (driver.page_source)
'''