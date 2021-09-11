# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : hm_04_类方法.py
"""


# 1. 定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    # 定义私有属性，以双下划线开头
    __tooth = 10

    # 定义类方法,以@classmethod修饰器修饰
    @classmethod
    def get_tooth(cls):
        return cls.__tooth


# 2. 创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)
