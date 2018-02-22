# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:11:42 2018

@author: msit11125
"""
## Matplotlib 圖表套件
#import matplotlib.pyplot as plt
#listx = [1,2,3]
#listy = [10,20,30]
#plt.plot(listx,listy)
#plt.show()


# Json String 轉dictionary
import requests , json
data = json.loads(
'''
{
   "book": {
      "id": 101,
      "title": "example glossary",
      "content": "blah blah blah..."
   }
}
'''
)

print( isinstance(data,dict))
print(data['book']['id'])