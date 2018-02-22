# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:29:24 2017

@author: msit11125
"""

import random as rnd

def SayHello(message):
    return "Hello! " + str(message)
def ctof(c):
    f = c * 1.8 +32
    return f    

s = SayHello("John Cena")
temperature = 30.5
s += ", 目前的華氏溫度 :" + str(ctof(temperature))
print(s)



def GetArea(width,height=10):
    return width * height

ret1 = GetArea(6) # 60
ret2 = GetArea(height=20,width=10) # 200

# 不定數目參數函式

def add(*params):
    global total #函式內宣告全域變數
    total = 0
    for param in params:
        total+= param
    return total

print("1+2+3+4+5 = " + str( add(1,2,3,4,5) ) )

# 三元運算
print(total) if total == 15 else print("加總錯誤")
    


if(1 != 2):
    print("not 1 == 2")

math = pow(2,3)  #2的3次方
math = pow(2,3,3)  #2的3次方，除以3的餘數
print(math)

pi = round(3.1415926535,2) # 四捨六入 3.14
print(pi)

list1 = [5,7,1,3,9]


list1.sort()  #一般排序
print(list1)  
list1.reverse()  #一般排序
print(list1)  

print("max= %d" % max(list1))
print("sum= %d" % sum(list1))
list2 = sorted(list1, reverse=True) # 內建函式排序 第二參數為大到小
print(list2)


print( 
       int(rnd.random()*10 + 1)
      )










