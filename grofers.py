import requests 
from pprint import pprint
from bs4 import BeautifulSoup 
inp=input("Enter the product name")
URL = "https://grofers.com/s/?q="+inp+"&suggestion_type=0&t=1"
r = requests.get(URL) 
soup = BeautifulSoup(r.text,'lxml') 
var=soup.findAll("div",class_="plp-product")
for ele in var:
    var2=ele.find("div",class_="plp-product__name ")
    var3=ele.find("span",class_="plp-product__price--new")
    print(var2['title'],var3.get_text())
