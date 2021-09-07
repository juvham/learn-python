#!/usr/bin/python
# -*- coding: utf-8 -*-

# 列表相关函数 重点


varlist = ['刘德华', '张学友', '张国荣', '张学友', '黎明', '郭富城', '小沈阳', '刘能', '宋小宝', '赵四']

# len()  检测当前列表的长度，列表中元素的个数
res = len(varlist)
print(res)

# count() 检测当前列表中指定元素出现的次数
res = varlist.count('张学友')
print(res)
# append() 向列表的尾部追加新的元素，返回值为 None
varlist.append('川哥')
print(varlist)
# insert() 可以向列表中指定的索引位置添加新的元素，
varlist.insert(20, 'aa')
print(varlist)

# pop() 可以对指定索引位置上的元素做 出栈 操作，返回出栈的元素
res = varlist.pop()  # 默认会把列表中的最后一个元素 出栈
print(res)
print(varlist)
res = varlist.pop(2)  # 会在列表中把指定索引的元素进行 出栈
print(res)
print(varlist)
varlist = [1, 2, 3, 4, 11, 22, 33, 44, 1, 2, 3, 4]
# remove() 可以指定列表中的元素 进行 删除,只删除第一个。如果没有找到，则报错
res = varlist.remove(1)
print(varlist)

# index() 可以查找指定元素在列表中第一次出现的索引位置
# res = varlist.index(1)
# res = varlist.index(1,5,20) # 可以在指定索引范围内查找元素的索引位置

# extend() 接收一个容器类型的数据，把容器中的元素追加到原列表中
# varlist.extend('123')

# s.clear() # 清空列表内容
# varlist.clear()


# reverse() 列表翻转
varlist.reverse()

# sort() 对列表进行排序
res = varlist.sort()  # 默认对元素进行从小到大的排序
res = varlist.sort(reverse=True)  # 对元素进行从大到小的排序
res = varlist.sort(key=abs)  # 可以传递一个函数，按照函数的处理结果进行排序


# copy()  拷贝，复制当前的列表、
varlist = ['a', 'b', 'c']
res = varlist.copy()

# 对copy后的列表进行操作
del res[2]
'''
['a', 'b']
['a', 'b', 'c']
'''

# 定义 多维列表
varlist = ['a', 'b', 'c', [11, 22, 33]]

res = varlist.copy()

# 对copy的列表进行一个操作
# del res[1] # 对一维列表进行操作，没有问题
del res[3][1]  # 对多维列表中的元素，进行操作，则出现了，全部改变的情况

print(res)
print(varlist)
