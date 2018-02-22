# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:59:04 2018

@author: msit11125
"""

def clickme():
    global count #接收全域的count變數
    count += 1
    btnVar.set("按過了")
    labelVar.set("你按了{}次".format(count))
    
import tkinter as tk



win = tk.Tk()
win.geometry("450x100")
win.title("這是主視窗")

count = 0
btnVar = tk.StringVar()
labelVar = tk.StringVar()

label1 = tk.Label(win,
                  text="標籤元件",
                  fg="red", 
                  bg= "yellow", 
                  font=("新細明體",12),
                  padx=20, # padding
                  pady=10,
                  textvariable =labelVar)

button1 = tk.Button(win,
                    textvariable=btnVar,
                    command=clickme)
btnVar.set("按我")
labelVar.set("你按了{}次".format(0))

label1.pack()
button1.pack()

win.mainloop()