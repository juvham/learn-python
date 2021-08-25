#!/usr/bin/python
# -*- coding: utf-8 -*-

# 字符串查找  重点重点重点重点


vars = 'iloveyoutosimidaandilikeyou'

# 检测一个字符串是否存在与一个字符串中
res = 'loves' in vars
print(res)
# 获取字符串的长度 len()
res = len(vars)
print(res)

# (1) 字符串查找相关函数

# 从左向右 获取指定字符在字符串中第一次出现的索引位置，未找到则返回 -1
# str.find(sub[, start[, end]])
res = vars.find('you')
print(res)
res = vars.find('you', 10, 27)
print(res)


# 从右向左 获取指定字符在字符串中第一次出现的索引位置，未找到则返回 -1
res = vars.rfind('you')
print(res)
res = vars.rfind('you', 0, 10)
print(res)

# str.index() 和find方法一样，只不过如果没有找到则报错 # ValueError: substring not found
res = vars.index('you')
print(res)
# str.rindex() 和 rfind方法一样，没有找到则引发异常 # ValueError: substring not found
res = vars.rindex('you')
print(res)

# str.count(sub[, start[, end]])# 统计一个字符在字符串中出现的字符
res = vars.count('you')
print(res)

# print(res)
