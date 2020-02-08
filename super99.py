import requests 
from bs4 import BeautifulSoup 
URL = "https://www.super99.in/catalogsearch/result/?q="
inp=input("Enter product you want to search for ")
r = requests.get(URL+inp) 
soup = BeautifulSoup(r.content, 'html.parser') 

var=soup.findAll('li',class_='item last')
for ele in var:
    var2=ele.find('h2',class_='product-name')
    var3=var2.find('a')
    var4=ele.find('span',class_='price')
    print(var3['title'],var4.get_text())
    
