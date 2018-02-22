# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:08:15 2018

@author: msit11125
"""

import os
import shutil  # 更強大的跨平台檔案處理套件 (同os)
import glob

cur_path = os.path.dirname(__file__) # 取得目前路徑

sample_tree = os.walk(cur_path)

for dirname,subdir,files in sample_tree:
    print("檔案路徑:",dirname)
    print("目錄串列:",subdir)
    print("檔案串列:",files)
    

# 複製 myFile.txt 為 myFile(複製).txt
destfile = cur_path +"\\dir2\\" + "myFile(複製).txt"
shutil.copy( cur_path +"\\dir2\\myFile.txt", destfile) #檔案複製
    

files = glob.glob("*.txt") + glob.glob("*.py")
for file in files:
    print(file)
    
