#!/usr/bin/python
# -*- coding: utf-8 -*-

# 匿名函数  lambda 表达式

'''
语法：
lambda [参数列表]:返回值
'''

# 封装一个函数做加法运算
# 普通函数
def jia(x,y):
    return x+y

# print(jia(2,3))

# 改成lambda表达式来封装
res = lambda x,y:x+y
# print(res(4,4))

# lambda是一个表达式，因为不能写太复杂的逻辑，功能相对单一
# lambda是否可以使用分支结构
def func(sex):
    if sex == '男':
        return '很man'
    else:
        return '很nice'

# res = func('男')
# print(res)

# 带有分支结构的lambda 表达式
#  lambda 参数列表: 真区间 if 表达式判断 else 假区间
res = lambda sex:"很man" if sex=='男' else "很nice"
print(res('女'))