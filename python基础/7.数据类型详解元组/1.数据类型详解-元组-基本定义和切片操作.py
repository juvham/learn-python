#!/usr/bin/python
# -*- coding: utf-8 -*-

# 元组的基本定义和切片操作


# 注意，定义元组时，如果只有一个元素，也需要使用 逗号
# vart = (1,)
# print(vart,type(vart))


# 元组的切片操作  和列表是一样的
vart = (1,2,3,4,5,5,4,3,2,1)
res = vart[:]  # 获取全部
print(res)

res = vart[::] # 获取全部
print(res)

res = vart[1:] # 从索引1开始获取到最后
print(res)

res = vart[1:3] # 从索引1开始到索引3之前
print(res)

res = vart[:3]   # 从索引 0 开始 到 索引 3之前
print(res)

res = vart[1:5:2] # 从索引1开始到索引5之前，步进值为2
print(res)

res = vart[::2]  # 从索引 0 开始 到 最后 ，步进值为2
print(res)

res = vart[5:1:-1] # 从索引5开始 到索引 1，步进值为-1  倒着输出
print(res)



# 获取元组的长度 len()
res = len(vart)
print(res)

# 统计一个元素在元组中出现的次数
res = vart.count(5)
print(res)


vart = ('张学友','吴恩达','柳岩','吴恩达')
# 获取一个元素在元组的索引值
res = vart.index('吴恩达')
print(res)

res = vart.index('吴恩达',2) # 从指定下标位置开始查找
print(res)

res = vart.index('吴恩达',2,5) # 从指定的 索引区间内 查找
print(res)


# 元组的 + * 运算 ，合并元组，组成新的元组
res = (1,2,3) + ('a','b')
print(res)

res = (1,2,3) * 3
print(res)


# 检测一个元素是否在元组中
# res = 22 in res
res = 22 not in res

print(res)
