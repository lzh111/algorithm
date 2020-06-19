#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2020/6/19 14:57
# @Author : 刘子豪
# @Version：V 0.1
# @File : 0001_getitem.py
# @desc :
class MyClass(object):
    """
    __getitem__拦截索引运算符：当实例X出现在X【i】这样的索引运算中时，
    Python会调用这个实例继承的__getitem__方法（如果有的话）
    把X作为第一个参数传递，并且方括号内的索引值传给第二个参数
    before python 2.2
    for ... in ... 也是会调用__getitem__() 方法
    要想是想类类对象的可迭代，需要手动实现__getitem__()方法
    """

    def __init__(self):
        self.item = 1211

    # def __getitem__(self, index):
    #     return index * 2  # 返回索引属性相关值

    def __getitem__(self, index):
        return self.fruits[index]  # 返回可迭代对象


myclass = MyClass()

# print(dir(myclass))
# print(myclass[2])

myclass.fruits = ["apple", "pear"]
for i in myclass:
    print(i)