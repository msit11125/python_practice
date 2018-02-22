# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:51:03 2017

@author: msit11125
"""


a=1 #此為註解
b=2
del b #清除記憶體
print(a+2)


num1 = 20
num2 = 20.50

flag = True 

print("多吃水果")
print(100,"多吃水果", 60)
print(100,"多吃水果", 60, sep="&")
print(100,"多吃水果", 60, sep="&",end="") #下次列印於同一行
print("多吃水果")

name = "小明"
score = 80
print("%s 的成績為 %d" % (name,score) )
print("{} 的成績為 {}".format(name,score) )

print(type(55))
print(type("Hello"))
print(type(True))

str1 = "Hello Python World"
subStr1 = str1[:5] # substring 結果 Hello
subStr2 = str1[2:7] # llo P

num1 = 5 + 7.8 #結果為12.8，浮點數
num2 = 5 + True #結果為6，整數
num3 = 23 + int("67")

score = 57
print("小明的成績是" + str(score))

if(score>=60 and score<=100):
    grade = "及格"
elif(score<60):
    grade = "不及格"
else:
    grade = "無效的成績"
print(grade) #判斷式外的下一行程式碼

        
list1 = [1,2,3,4,5] #元素皆為整數
list2 = ["香蕉","蘋果","橘子"] #元素皆為字串
list3 = [1,"香蕉",True] #包含不同資料型態元素
print(list3[2])
print(list3[-1])  #可以是負數從後面取出True，此陣列最多到-3

list4 =[["joe","1234"],["mary","abcd"],["david","5678"]]
print(list4[1][1]) #印出abcd

score = [85,79,93]
print("國文成績:%d分" % score[0])
print("數學成績:%d分" % score[1])
print("英文成績:%d分" % score[2])

list1 = range(5) #產生list1 = [0,1,2,3,4]
list2 = range(3,8) #產生list1 = [3,4,5,6,7]
list3 = range(3,8,2) #(起始值,終止值,間隔值) 產生#list1 =[3,5,7]
list4 = range(8,3,-2) #(起始值,終止值,間隔值) 產生#list1 =[8,6,4]

# -------- 聖誕樹 -----------
for i in list1:
    print(i,end=",")
    
print("",end="\n")  
for i in range(0,10):  
    for s in range(10,i,-1):
        print(" ",end="")
    for j in range(0,i*2-1):
        print("*",end="")
    print("",end="\n")
    
    
# -------- 九九乘法表 -----------
for i in range(1,10):
    for j in range(i,10):
        product = i * j
        print("%d * %d = %-2d   " % (i,j,product),end="")   #-2d占兩字元 
    print()

# -------- 判斷質數 for...else... -----------
n = 121
if(n==2):
    print("2是質數!")
else:
    for i in range(2,n):
        if(n % i == 0):
            print("%d不是質數!" % n)
            break
    else:
        print("%d是質數!" % n)

total = n = 0
while (n < 10):
    total += n
    n += 1
print(total) # 1+2+3....+9 = 45
 
total = 0       
score = [80,85,92,94,88]
for i in range(0,len(score)):
    total += score[i]
print(total)      


list1 = [1,2,3,4,5,6]
list1.append([7,8]) # result: [1,2,3,4,5,6,[7,8]]
list1.extend([9,10]) # result: [1,2,3,4,5,6,[7,8],9,10]
n = list1.pop(3) # n=4


# ------- 元組(Tuple) -------
tuple1 = (1,2,3,4,5) #元素皆為整數
tuple1 = (1,"香蕉",True) #包含不同資料型態元素

tuple3 = ("香蕉","蘋果","橘子")
print(tuple3[1]) #蘋果
#tuple3[1] = "芭樂" #錯誤，元素質不能修改
#tuple3.append("芭樂")  #錯誤，不能增加元素

list1 = list(tuple1) #元組轉為串列
tuple2 = tuple(list1) #串列轉為元組

# ------- 字典(Dict) -------
dict1 = { "香蕉":20 , "蘋果":50 , "橘子":30 , "香蕉":200 }
print("蘋果價格 : "+ str(dict1["蘋果"]) ) #50
n = dict1.get("蘋果") # n = 50
n = dict1.get("西瓜你個芭樂") # n = None
n = dict1.get("西瓜你個芭樂" , 10000) # n = 10000 沒有key時回傳預設值

s = dict1.setdefault("西瓜你個芭樂", 10000) # setdefault 字典內會多 西瓜你個芭樂
print(dict1)

print(dict1["香蕉"]) #200 >>相同key取最後的值
dict1["橘子"] = 60
dict1["鳳梨"] = 60 #新增元素
print(dict1)


del dict1["鳳梨"] #刪除字典特定元素
dict1.clear() #刪除字典全部元素

dict1 = { "林小明":85 , "曾山水":93 , "鄭美麗":67 }
listkey = list(dict1.keys()) # ["林小明","曾山水","鄭美麗"]
listvalue = list(dict1.values()) # [85,93,67]
for i in range(len(listkey)):
    print("%s 的成績為%d分" % (listkey[i] , listvalue[i]))
    
find = "林小明" in dict1 # find = true



# 字串轉Dictionary套件
import ast

strDic = '''{ "apple": 15 ,"banana": 20 }'''
dictionary = ast.literal_eval(strDic)

for key in dictionary:
    print("{}\t{}".format(key,dictionary[key]) )
    
del dictionary['apple'] # 刪除
