#!/usr/bin/python
# -*- coding: utf-8 -*-

# 数学相关函数

# 获取一个数的绝对值
print(abs(-99.99))

# 求和 从 start 开始自左向右对 iterable 中的项求和并返回总计值
print(sum([1, 2, 3]))

# 获取最大值
print(max([1, 2, 3]))
print(max(99, 12, 45))

# 获取最小值
print(min([2, 1, 6, -9]))
print(min(6, 7, 1, 0, -2))

# 幂运算  返回 x 的 y 次幂
print(pow(2, 3))

# 四舍五入
r = round(3.1415926)
r = round(3.1415926, 2)  # 小数点保留几位

r = round(4.5)  # 奇进偶退  1.5 = 2 2.5=2,3.5=4,4.5=4
print(r)
