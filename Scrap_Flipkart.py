#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4  import BeautifulSoup
import pandas
from pprint import pprint
r=requests.get("https://www.flipkart.com/search?q=lamps&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
c=r.content
soup=BeautifulSoup(c,"html.parser")
top=soup.find_all("div",class_="_3liAhj")
records=[]
for ele in top:
    name=ele.find("a","title",class_="_2cLu-l")
    price=ele.find("div",class_="_1vC4OE")
    records.append((name['title'],price.get_text()))

for ele in records:
    print(ele)
print(len(records))


# In[2]:


import requests
from bs4  import BeautifulSoup
import pandas
from pprint import pprint
r=requests.get("https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=shoes&requestId=bcb26a16-f99f-441d-87bc-a6cb6226c925")
c=r.content
soup=BeautifulSoup(c,"html.parser")
top=soup.find_all("div",class_="IIdQZO _1SSAGr")
records=[]
for ele in top:
    name=ele.find("a","title",class_="_2mylT6")
    price=ele.find("div",class_="_1vC4OE")
    records.append((name['title'],price.get_text()))

for ele in records:
    print(ele)
print(len(records))


# In[ ]:




