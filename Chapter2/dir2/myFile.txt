# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:33:35 2017

@author: msit11125
"""


import os

# ------remove方法------
file = "myFile.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print(file + "檔案未建立!")
    

# ------建立資料夾------
mydir = "dir1"
if not os.path.exists(mydir):
    os.mkdir(mydir)   #在目前位置建立dir1目錄
else:
    print(mydir + "已經建立!")    

# ------移除資料夾------
if os.path.exists(mydir):
    os.rmdir(mydir)
else:
    print(mydir + "目錄未建立")

# ------執行作業系統命令------
cur_path = os.path.dirname(__file__) # 取得目前目錄的路徑  __file__:此份.py檔案的絕對位置

os.system("cls") # 清除螢幕
os.system("mkdir dir2") # 建立dir2目錄
os.system("copy AccessFile.py dir2\myFile.txt") #複製檔案

file = cur_path + "\dir2\myFile.txt"
os.system("notepad " + file) #用記事本開啟copyfile.py檔案


filename = os.path.abspath("AccessFile.py")
if os.path.exists(filename):
    print("完整路徑名稱: " , filename)
    print("檔案大小: " , os.path.getsize)
    
    basename = os.path.basename(filename) #最後的檔案或路徑名稱
    dirname = os.path.dirname(filename) #目前檔案目錄路徑
    isdir = os.path.isdir(filename) #是否為目錄
    fullpath,fname = os.path.split(filename)
    print("目錄路徑: ", fullpath , "\n檔名: ", fname)
    Drive,fpath = os.path.splitdrive(filename)
    print("磁碟機: " , Drive)
    print("路徑名稱: " , Drive)
    fullpath = os.path.join(fullpath + "\\" + fname)
    print("組合路徑: " , fullpath)
    











    