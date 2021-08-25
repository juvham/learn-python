#!/usr/bin/python
# -*- coding: utf-8 -*-

# range() 函数

'''
range()函数
功能：能够生成一个指定的数字序列
参数：
    start : 开始的值 ，默认值为0
    stop  ： 结束的值
    [, step]： 可选，步进值 默认值为1
返回值： 可迭代的对象，数字序列
'''
# 获取range函数返回的数字序列的方法
# res = range(10)
# 1。转为list列表数据
# print(list(res))

# 2。通过 for循环 进行遍历
# for i in res:
#     print(i)

# 3。转为迭代器，使用next函数调用
# res = iter(res)
# print(next(res))
# print(next(res))


#range函数的使用方式
# 只写一个参数，就是从零开始到10之前，9
# res = range(11)

# 两个参数时，第一个参数是开始的值，第二个参数是结束的值（在结束值之前）
# res = range(5,10)

# 三个参数， 参数1是开始值，参数2是结束值，参数三是步进值
# res = range(1,10,3)

# 获取一个倒叙的数字序列
# res = range(10,0,-1)
# res = range(10,0,-2)

res = range(-10,-20,-1)
res = range(-20,-10)
res = range(-10,10)
print(list(res))


# 这是第二个函数的介绍
# zip(), 压缩函数，压缩数据，组成一个新的数据格式





