# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:12:07 2018

@author: msit11125
"""

# 網址解析套件
from urllib.parse import urlparse
url = 'http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1'

o = urlparse(url)
print(o)

print("scheme={}".format(o.scheme))


# 網頁資料擷取
import requests
from bs4 import BeautifulSoup


url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding = 'utf-8'

html_list = html.text.splitlines()
n=0
for row in html_list:
    if "程式設計" in row: n+=1

print("找到{}次。".format(n))

sp = BeautifulSoup(html.text, 'html.parser')
imgs = sp.select("img")
print(imgs)

divOne =sp.find('div', { 'class':''})  # 找第一筆符合的
print(len(divOne)) # => 0

divs =sp.find_all('div', { 'class':''})  # 找全部符合的
print(len(divs)) # => 7


divlist = []
divlist.append(divOne)
divlist.extend(divs)

print(len(divlist))



