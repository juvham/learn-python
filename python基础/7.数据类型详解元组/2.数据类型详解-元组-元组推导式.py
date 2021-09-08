#!/usr/bin/python
# -*- coding: utf-8 -*-

#  元组推导式  生成器
'''
元组推导式
    列表推导式结果返回了一个列表，元组推导式返回的是生成器
    语法：
        列表推导式 ==> [变量运算 for i in 容器]  ==> 结果 是一个 列表
        元组推导式 ==> (变量运算 for i in 容器)  ==> 结果 是一个 生成器

生成器是什么？
    生成器是一个特殊的迭代器，生成器可以自定义，也可以使用元组推导式去定义
    生成器是按照某种算法去推算下一个数据或结果，只需要往内存中存储一个生成器，节约内存消耗，提升性能
语法：
    （1） 里面是推导式，外面是一个() 的结果就是一个生成器
     (2) 自定义生成器，含有yield关键字的函数就是生成器
         含有 yield 关键字的函数，返回的结果是一个迭代器，换句话说，生成器函数就是一个返回迭代器的函数

如何使用操作生成器？
    生成器是迭代器的一种，因此可以使用迭代器的操作方法来操作生成器
'''

# 列表推导式
varlist = [1,2,3,4,5,6,7,8,9]
# newlist = [i**2 for i in varlist]
# print(newlist) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 元组推导式 生成器 generator
newt = (i**2 for i in varlist)
print(newt) # <generator object <genexpr> at 0x1104cd4d0>

# 使用next函数去调用
print(next(newt))
print(next(newt))

# 使用list或tuple函数进行操作
print(list(newt))
print(tuple(newt))

# 使用 for 进行遍历
for i  in newt:
    print(i)

