#!/usr/bin/python
# -*- coding: utf-8 -*-

# tuple 元组类型

'''
+ 在定义多个数据内容时，可以选择使用List列表类型
+ 还可以使用元组类型来定义，元组和列表非常像，都时用于存储多个数据时使用
+ 元组使用小括号进行定义（），列表使用中括号进行定义
'''
# tuple
vart = (1,2,3,'a','b')
# print(vart,type(vart))
# print(vart[3])

# 注意在定义元组时，如果元组中只有一个元素，那么需要加, 不然就不是元组类型了
# vart = (123,)

# 元组的其它定义方式
vart = 1,2,3
# print(vart,type(vart))

# 列表与元组的区别
'''
+ 列表使用中括号定义，
+ 元组使用小括号定义，
+ 列表中的值可以被改变，
+ 元组中的值是不可以改变的
'''
# 定义列表
varl = [1,2,3]
# 通过下标来修改元素的值
varl[2] = 33
# print(varl)

# 定义元组
vart = (1,2,3)
vart[2] = 33
print(vart) #  错误，元组的值不能改变
# 'tuple' object does not support item assignment