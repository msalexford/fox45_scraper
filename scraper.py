import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re

headless_options = Options()
headless_options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=headless_options)

driver.get('https://foxbaltimore.com/')
driver.set_page_load_timeout(30)

fox_results = []

scraped_date = driver.find_element_by_xpath('/html/head/meta[30]').get_attribute('content')

homepage = driver.find_elements_by_xpath("//*[contains(@id, 'js-TopStories-Container')]")

for link in homepage:
    print(link.text, scraped_date)
    
headlines = link.text.splitlines()

df = pd.DataFrame(headlines)

pd.read_csv('fox45_headlines.csv').append(df).drop_duplicates().to_csv('fox45_headlines.csv', sep=',', header=None, index=None)

# df.to_csv('fox45_headlines.csv', sep=',', header=None, index=None)
