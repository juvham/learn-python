#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# zip() 函数

'''
zip()
功能：zip 函数是可以接受多个可迭代的对象，然后把每个可迭代对象中的第i个元素组合在一起，形成一个新的迭代器
参数：*iterables，任意个的 可迭代对象
返回值： 返回一个元组的迭代器
'''

var1 = '1234'
var2 = ['a','b','c']
var3 = ('A','B','C','D')
# 调用zip函数，组成新的元组迭代器
res = zip(var1,var2,var3)
# print(res,type(res))

# 提取迭代器数据的方法， next(),list(),for i in ...
# print(list(res))
'''
[
    ('1', 'a', 'A'), 
    ('2', 'b', 'B'), 
    ('3', 'c', 'C'), 
    ('4', 'd', 'D')
]
'''
# for i in res:
#     print(i)
'''
('1', 'a', 'A')
('2', 'b', 'B')
('3', 'c', 'C')
('4', 'd', 'D')
'''
# v1 = [1,2,3,4]
# v2 = [22,33,44,55]
# res = zip(v1,v2)
# print(list(res))
'''
[
    (1, 22), 
    (2, 33), 
    (3, 44), 
    (4, 55)
]
'''
# zip() 与 * 运算符相结合可以用来拆解一个列表:
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))

print(zip(x, y)) # 迭代器对象，
print(*zip(x, y))# 组合好的多个元组数据

x2, y2 = zip(*zip(x, y))
print(x2,y2)
# (1, 2, 3) (4, 5, 6)
