#-*- coding: utf-8 -*-
'''
@author: birdlin
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver.get("http://www.python.org")
#assert "Morningstar" in driver.title
assert 'Python' in driver.title
#soup = BeautifulSoup(driver.page_source, 'lxml')
#for title in soup.find_all('td'):
#    print (title)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to_window(driver.window_handles[1])

driver.get("http://www.yahoo.com")
assert 'Yahoo' in driver.title

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.switch_to_window(driver.window_handles[2])

driver.get('http://financials.morningstar.com/ratios/r.html?t=UA&region=USA&culture=en_US')
assert "Morningstar" in driver.title

driver.switch_to_window(driver.window_handles[0])
driver.close()

driver.switch_to_window(driver.window_handles[1])
driver.close()
