#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# filter() 过滤器

'''
filter(func,iterable)
功能： 过滤数据，把 iterable 中的每个元素拿到 func 函数中进行处理，
        如果函数返回True则保留这个数据，返回False则丢弃这个数据
参数：
    func  自定义函数
    itereble： 可迭代的数据
返回值：保留下来的数据组成的 迭代器
'''

# 要求 保留所有的偶数，丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9]

# 普通方法实现
# newlist = []
# for i in varlist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)

# 使用 filter 进行处理

# 定义一个函数，判断当前这个函数是否为偶数，偶数返回True，奇数返回False
# def myfunc(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# # 调用 过滤器 函数进行处理
# it = filter(myfunc,varlist)
# print(it,list(it))

# 优化版
it = filter(lambda n:True if n % 2 == 0 else False,varlist)
print(it,list(it))



