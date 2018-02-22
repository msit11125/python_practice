# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:29:02 2018

@author: msit11125
"""
import locale

print(locale.getdefaultlocale())


# 模式 r:讀取 w:寫入(覆蓋) a:附加
# 編碼
f = open('text.txt','w',encoding = 'utf-8') 

content = '''測試寫入文字
Hello Python'''

f.write(content)
f.close()

# with 同f.close()
with open('text.txt','r',encoding = 'utf-8') as f:
    for line in f:
        print(line,end="")
    
with open('text.txt','r',encoding = 'utf-8') as f:
    content = f.readlines()
    print(type(content))
    print(content)

