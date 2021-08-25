#!/usr/bin/python
# -*- coding: utf-8 -*-

# Dict 字典类型

'''
+ 字典也是用于存储一组或多组数据时使用，使用大括号 {}来定义
+ 字典是 键值对 的存储方式 name ：admin
+ 键和值之间使用冒号进行分隔，多组键值对之间使用逗号分隔
+ 键必须是字符串或数字类型，值可以是任意类型
+ 键名不能重复，值可以重复
'''
# 比如需要记录一本书的相关数据 书名，作者，价格，。。。
vard = {'title':'<<鬼谷子>>','author':'鬼谷子','price':'29.99'}
# print(vard,type(vard))
# {'title': '<<鬼谷子>>', 'author': '鬼谷子', 'price': '29.99'} <class 'dict'>

# 获取字典中的值
# print(vard['title'])

# 字典中的键不能重复使用，否则会覆盖
vard = {'a':10,'b':10,'c':20,'a':'aa',1:'abcdef','2':'2222'}
print(vard)

# tip: 在python之前的版本中，字典是无序的