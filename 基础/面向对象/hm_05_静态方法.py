# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : hm_05_静态方法.py
"""


# 1. 定义类，定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')


# 2. 创建对象
wangcai = Dog()
# 3. 调用静态方法：类 和 对象
wangcai.info_print()
Dog.info_print()
