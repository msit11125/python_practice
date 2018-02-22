# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:56:24 2018

@author: msit11125
"""

import hashlib

print(b'A' == b'\x41') # b string => 轉byte

before = b'Hello'
print(before)

md5 = hashlib.md5(before).hexdigest() # md5加密
print(md5)
