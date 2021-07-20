#!/usr/bin/env python
# coding: utf-8

# In this attempt, I am trying to get the Chrome Driver to install in GH Actions
# using the ChromeDriverManager

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re

# Adding headless options to avoid opening the webpage.

headless_options = Options()
headless_options.add_argument('--headless')

# Installing the driver with the headless options.

driver = webdriver.Chrome(ChromeDriverManager().install(), options=headless_options)

# Accessing the Fox website.

driver.get('https://foxbaltimore.com/')
driver.set_page_load_timeout(30)

# Calling headlines using xpath.

homepage = driver.find_elements_by_xpath("//*[contains(@id, 'js-TopStories-Container')]")
for link in homepage:
    print(link.text)
    
# Formatting the values into a list.

headlines = link.text.splitlines()
df = pd.DataFrame(headlines)

# print(df)

# Export as CSV.

df.to_csv('fox45_headlines.csv', sep=',', header=None, index=None)

