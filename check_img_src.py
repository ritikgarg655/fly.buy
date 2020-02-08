from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

driver = webdriver.chrome()
# it takes forever to load the page, therefore we are setting a threshold
driver.set_page_load_timeout(5)
inp=input("Enter the product name")
URL = "https://grofers.com/s/?q="+inp+"&suggestion_type=0&t=1"

try:
    driver.get("URL")
except TimeoutException:
    # never ignore exceptions silently in real world code
    pass

soup2 = BeautifulSoup(driver.page_source, 'html.parser')
divImage = soup2.find('div', class_ = "plp-product")

# close the browser 
driver.close()

for img in divImage.findAll('img'):
    print (img.get('src'))
