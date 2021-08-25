#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 高阶函数 map()

# 对传入的可迭代数据中的每个元素进行处理，返回一个新的迭代器

'''
map(func, *iterables)
功能： 对传入的可迭代数据中的每个元素放入到函数中进行处理，返回一个新的迭代器
参数：
    func 函数  自定义函数|内置函数
    iterables：可迭代的数据
返回值：迭代器
'''

# （1）把一个字符串数字的列表转为 整型的数字列表
# ['1','2','3','4']  # ==> [1,2,3,4]
# 普通的处理方法
# varlist = ['1','2','3','4']  # ==> [1,2,3,4]
# newlist = []
# for i in varlist:
#     newlist.append(int(i))
# print(newlist)

# 使用map函数进行处理
# varlist = ['1','2','3','4']
# res = map(int,varlist) # <map object at 0x104ea8890>
# print(list(res))

# (2) [1,2,3,4] ==> [1,4,9,16]

# 普通方法
# varlist = [1,2,3,4]
# newlist = []
# for i in varlist:
#     res = i ** 2
#     newlist.append(res)
# print(newlist)

# 使用map函数处理这个数据
varlist = [1,2,3,4]
# def myfunc(x):
#     return x ** 2
# res = map(myfunc,varlist)
# print(res,list(res))

# 优化版
res = map(lambda x:x**2,varlist)
print(res,list(res))


# 练习作业
# (3) ['a','b','c','d'] ==> [65,66,67,68]
