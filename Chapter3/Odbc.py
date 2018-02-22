# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:12:50 2018

@author: msit11125
"""

import pyodbc 
conn_str = (
    r"Driver={SQL Server Native Client 11.0};"  # r => raw
    r"Server=(localdb)\ApiSample;"
    r"Database=Northwind;"
    r"Trusted_Connection=yes;"
    #r'UID=user;'
    #r'PWD=password'
    )


cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
# ? => 防sql injection    
cursor.execute("select * from [Northwind].[dbo].[Products] WHERE ProductID = ?" , "1")

# 一列一列讀取
#row = cursor.fetchone() 
#while row: 
#    print("ProductID:{}".format(row[0]))
#    row = cursor.fetchone()
    

# 一次讀取
results = []
rows = cursor.fetchall()

# 欄位名稱
columns = [column[0] for column in cursor.description]

for row in rows:
    results.append(dict(zip(columns, row)))

print(results)





    