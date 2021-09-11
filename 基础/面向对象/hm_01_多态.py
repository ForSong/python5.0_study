# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : hm_01_多态.py
"""


# 需求：景物人员和警犬一起工作，警犬分两种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作

# 多态步骤：
# 将需求套入多态步骤
# 如何决定类的数量：1. 首先看需求中有几个事物 2. 将事物向上抽象，获得类
# 经过分析，这里的警犬类有父类和子类而人这个类没有父类和子类，因此先将警犬这个类梳理清楚，再去定义人这个类

# 1. 定义父类，提供公共方法：警犬类 和 人
# 首先定义警犬的父类
class Dog(object):
    def work(self):
        pass  # 因为后面会重写，这里只需要占位即可


# 2. 定义子类，子类重写父类方法： 定义两个类表示不同的警犬
# 定义子类，追击敌人的狗
class ArmyDog(Dog):
    # 注意这里的参数是Dog，因为是集成的Dog类
    def work(self):
        print('追击敌人')


# 定义子类，缉毒犬
class DrugDog(Dog):
    def work(self):
        print('追查毒品')


# 定义人类
class Person(object):
    def work_with_dog(self, dog):  # 形参用于接收不同的犬类
        dog.work()


# 3. 创建对象，调用不同的功能，传入不同的对象，观察执行的结果
# 有多少个事物，就有多少个对象
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)  # 注意这里一定要记得传入对象实参
daqiu.work_with_dog(dd)  # 注意这里一定要记得传入对象实参
# 同样一个类Person，调用了同样的方法work_with_dog,传入了不同的参数，导致最后的结果不同
# 可以看到Person类更加通用了