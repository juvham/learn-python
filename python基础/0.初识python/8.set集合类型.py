#!/usr/bin/python
# -*- coding: utf-8 -*-

# set集合类型

'''
+ set集合是一个 无序且元素不重复的 集合的数据类型
+ set集合使用 中括号或者set()方法来定义
'''

# 集合的定义方式
# vars = {1,2,3,'a','b',1}
# vars = set('123456')

# 如果需要定义一个空集合时 只能使用 set()方法,因为大括号时定义的空字典
# vars = {}
# vars = set()
# print(vars,type(vars)) # <class 'set'>

a = {1,2,3,'a'}
# 给集合添加元素
# a.add('b')
# 无法获取集合中的单个元素，但是可以添加和删除
# a.discard('a')
# print(a)
# 检查当前的元素是否在集合中
# print(1 in a)


# 集合主要用于运算，交集，差集，并集，对称集合
a = {1,2,3,'a','b'}
b = {1,'a',22,33}

print(a & b) # 交集  {1, 'a'}
print(a - b) # 差集 {'b', 2, 3}  a 集合有，b集合没有的
print(a | b) # 并集 {1, 2, 3, 33, 'a', 'b', 22} 两个集合，放到一起，并且去重
print(a ^ b) # 对称差集 {33, 2, 3, 'b', 22}
