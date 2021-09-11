# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : hm_02_设置和访问类属性.py
"""


# 1. 定义类，定义类属性
class Dog(object):
    toooth = 10


# 2. 创建对象
wangcai = Dog()
xiaohei = Dog()
# 3. 访问类属性：类和对象分别访问
print(Dog.toooth)
print(wangcai.toooth)
print(xiaohei.toooth)
