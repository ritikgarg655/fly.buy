import requests 
from bs4 import BeautifulSoup
from pprint import pprint
from tkinter import *
import pandas as pd
import csv

def printtext():
    global e
    string = e.get() 

def save_data(data,web_name):

    results=web_name
    file_name = "C:/Users/Purvansh/Desktop/"+results+".csv"
    with open(file_name, 'a',encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile) 
        for ele in data:
            csvwriter.writerow(ele)

def compare_prices(inp): 
    print("Super99 store has to offer...")
    URL = "https://www.super99.in/catalogsearch/result/index/?limit=60&q="
    r = requests.get(URL+inp) 
    soup = BeautifulSoup(r.content, 'html.parser') 
    var=soup.findAll('li',class_='item last')
    name_s99=[]
    price_s99=[]
    link_s99=[]
    Super99_list=[]
    for ele in var:
        var2=ele.find('h2',class_='product-name')
        var3=var2.find('a')
        var4=ele.find('span',class_='price')
        var4=var4.get_text().strip()
        name_s99.append(var3['title'])
        price_s99.append(var4)
        link_s99.append(var3['href'])
        Super99_list.append([var3['title'],str(var4.strip(var4[0])),var3['href']])
    Super99_table = pd.DataFrame(Super99_list, columns = ['Name' , 'Price', 'Link'])
    print(Super99_table)
    save_data(Super99_list,"Super99")
    
    print("***************************************************************************************************************t")
    print("Grofers store has to offer...")
    URL2 = "https://grofers.com/s/?q="+inp+"&suggestion_type=0&t=1"
    r = requests.get(URL2) 
    soup = BeautifulSoup(r.text,'lxml') 
    var=soup.findAll("div",class_="plp-product")
    r_cnt=0
    web_url="https://grofers.com"
    name_g=[]
    price_g=[]
    link_g=[]
    grofers_list=[]
    for ele in var:
        var2=ele.find("div",class_="plp-product__name ")
        var3=ele.find("span",class_="plp-product__price--new")
        var3=var3.get_text().strip()
        var4=soup.findAll('a',class_="product__wrapper")
        name_g.append(var2['title'])
        price_g.append(var3)
        link_g.append(web_url+var4[r_cnt]['href'])
        grofers_list.append([var2['title'],str(var3.strip(var3[0])),web_url+var4[r_cnt]['href']])
        r_cnt=r_cnt+1
    grofers_table = pd.DataFrame(grofers_list, columns = ['Name' , 'Price', 'Link'])
    print(grofers_table)
    save_data(grofers_list,"grofers")
    
root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    compare_prices(inputValue)

textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button

buttonCommit.pack()

mainloop()
