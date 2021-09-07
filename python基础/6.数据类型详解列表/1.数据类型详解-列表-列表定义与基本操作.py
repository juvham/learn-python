#!/usr/bin/python
# -*- coding: utf-8 -*-

# 列表定义与基本操作

varlist1 = [1, 2, 3, 4]
varlist2 = ['a', 'b', 'c', 'd']

# 列表的拼接。把多个列表的元素拼接成一个列表
res = varlist1+varlist2+[11, 22, 33]

print(res)

# 列表元素的重复
res = varlist1*3
print(res)
# 检测元素是否存在于列表
res = 'a' in varlist1
print(res)
# 列表的索引操作
'''
 0   1   2   3
'a','b','c','d'
-4  -3  -2  -1
'''
# 通过下标获取指定的元素
res = varlist2[2]
print(res)
res = varlist2[-3]
print(res)
# 通过下标修改元素
varlist2[2] = 'cc'
print(res)

# 不能通过下标添加元素,
# varlist2[4] = 'ff'  #IndexError: list assignment index out of range

# 向列表元素中追加元素
varlist2.append('ff')

print(varlist2)
# 列表元素的删除,通过下标进行元素的删除
del varlist2[2]
print(res)
res = varlist2.pop()
print(res)
# print(res)

# 获取列表的长度 len()
res = len(varlist2)

print(varlist2)
