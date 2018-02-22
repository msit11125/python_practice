# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:29:51 2018

@author: msit11125
"""

# ----- level 1 ----- 
# -------------------
import math

a= math.pow(2,38)

print(int(a))




# ----- level 2 ----- 
# -------------------
print(ord('a'))
hashstr = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj
'''

newstr = ""

i = 0
while i < len(hashstr):
    char = hashstr[i]
    if not char in ['.',' ','\'','(',')']:
        if char == 'y':
            char = 'a'
        elif char =='z':
            char = 'b'
        else:
            char = chr(ord(char) + 2 )
        
    i+=1
    newstr += char
        
print(newstr)


# 一樣的效果
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)
print(hashstr.translate(trantab))



# ----- level 3 ----- 
# -------------------
import urllib.request
import re
 
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

# find rare characters in the mess below: 在html裡面找到稀少的單字
comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
data = comments[-1]

count = {} #字典
for c in data:
    count[c] = count.get(c, 0) + 1 # 累計找到的次數+1，初始為0
    
print(count)

print("".join(re.findall("[A-Za-z]", data))) # equality


