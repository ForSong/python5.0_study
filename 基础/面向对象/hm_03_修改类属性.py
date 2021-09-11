# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : hm_03_修改类属性.py
"""


class Dog(object):
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

# 1. 类 类.类属性 = 值
Dog.tooth = 12
print('通过类修改类属性')
print(Dog.tooth)  # 12
print(wangcai.tooth)  # 12
print(xiaohei.tooth)  # 12

print('通过对象修改类属性：')
# 2. 测试通过对象修改类属性
wangcai.tooth = 20
print(Dog.tooth)  # 12
print(wangcai.tooth)  # 20
print(xiaohei.tooth)  # 12
