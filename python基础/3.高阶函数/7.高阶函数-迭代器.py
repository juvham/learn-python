#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 迭代器

# range(10,3,-1)  返回一个可迭代的对象，
# for i in range(10,3,-1):
#     print(i)

# arr = ['a','b','c',4,5]
# for i in arr:
#     print(i)


'''
iter()
    功能：把可迭代的对象，转为一个迭代器对象
    参数：可迭代的对象 （str，list，tuple，dict，set，range。。。）
    返回值： 迭代器对象
注意：迭代器一定是一个可以迭代的对象，但是可迭代对象不一定是迭代器
'''
# 定义一个列表，是一个可迭代的对象
f4 = ['赵四','刘能','小沈阳','海参炒面']
# 可以使用for循环来遍历数据

# 可以把可迭代对象转为迭代器使用
res = iter(f4)
# print(res,type(res)) # <list_iterator object at 0x109063810> <class 'list_iterator'>



# 取值方案
'''
迭代器取值的方案
    1。 next() 调用一次获取一次，直到数据被取完
    2。 list() 使用list函数直接取出迭代器中的所有数据
    3。 for    使用for循环遍历迭代器的数据
迭代器取值的特点，取出一个少一个，直到都取完，最后再获取就会报错
'''
# 1。 使用next()函数去调用迭代器对象
print(next(res))
print(next(res))


# 2。 使用list取值
r = list(res)
print(r)

# 3。 使用for循环
for i in res:
    print(i)

# print(next(res))  #  # 超出可迭代的范围  StopIteration

# 检测迭代器和可迭代对象的方法

from collections.abc import Iterator,Iterable

varstr = '123456'
res = iter(varstr)

# type() 函数返回当前数据的类型，
# isinstance() 检测一个数据是不是一个指定的类型
r1 = isinstance(varstr,Iterable) # True 可迭代对象
r2 = isinstance(varstr,Iterator) # False 不是一个迭代器
r3 = isinstance(res,Iterable) # True 可迭代对象
r4 = isinstance(res,Iterator) # True 是一个迭代器
print(r1,r2)
print(r3,r4)
# 迭代器一定是一个可迭代的对象，可迭代对象不一定是迭代器

# next(varstr) # TypeError: 'str' object is not an iterator




