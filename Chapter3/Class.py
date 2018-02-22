# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:33:32 2018

@author: msit11125
"""

# 參考範例
# http://yangcongchufang.com/%E9%AB%98%E7%BA%A7python%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/python-object-class.html

# 1. Class 用法 
class Student(object):
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    
    def __init__(self, name):
        self.__name = name      # 加上 __ 變成private屬性
        
    def printStdInfo(self):
        print("%s(%s)" % (std.__name, std.__score))
        
    def set_score(self, score = 100):
        if score>0:
            self.__score = score
        else:
            raise ValueError('錯誤的成績')


std = Student("John")

std.set_score(50)
std.printStdInfo()
print(std._Student__name) # 這樣就可以訪問private變量 但不建議這樣子做




# 2. 繼承和多型
class Animal(object):
    def run(self):
        print('running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')
    
class Cat(Animal):
    def run(self):
        print('Cat is running...')
    

dog = Dog()
dog.run()

print( isinstance(dog,list) ) # 判別type
print( isinstance(dog,(list, object)) ) # 判別是否為list或object
print( isinstance(dog,Animal) )



# 3. Enum

from enum import Enum, unique

#unique裝飾器幫助檢查保證沒有重複值
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

print(Weekday.Sun)
print(Weekday['Sun'])
print(Weekday(0))


list1 = list()
dog.abc = 123
list1.append(dog)

for dog in list1:
    print(dog.abc)