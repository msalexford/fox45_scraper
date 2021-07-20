#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

# Setting up the driver.

headless_options = Options()
headless_options.add_argument('--headless')

chrome_path = r'/Users/alexandraford1/Desktop/_Lede/selenium_project/chromedriver'
driver = webdriver.Chrome('/Users/alexandraford1/Desktop/_Lede/selenium_project/chromedriver', options=headless_options)
driver.get('https://foxbaltimore.com/')
driver.set_page_load_timeout(30)

# Calling headlines using xpath.

homepage = driver.find_elements_by_xpath("//*[contains(@id, 'js-TopStories-Container')]")
for link in homepage:
    print(link.text)
    
# Formatting the values into a list.

headlines = link.text.splitlines()

df = pd.DataFrame(headlines)

# Export as CSV.

df.to_csv('fox45_headlines.csv', sep=',', header=None, index=None)

