#!/usr/bin/python
# -*- coding: utf-8 -*-
# 列表推到式


# 一，基本的列表推到式使用方式
# 变量 = [变量或变量的处理结果 for 变量 in 容器类型数据]

# 1 假设我们想创建一个平方列表

# 使用普通方法完成
varlist = []
for i in range(10):
    varlist.append(i**2)
print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用 map函数和list完成
varlist = list(map(lambda x: x**2, range(10)))
# print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用列表推到式完成 下面这个列表推到式和第一种方式是一样的
varlist = [i**2 for i in range(10)]
# print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2。 '1234' ==> [2,4,6,8]
# 常规方法完成需求
varstr = '1234'
newlist = []
for i in varstr:
    newlist.append(int(i)*2)
# print(newlist)  # [2, 4, 6, 8]

# 使用列表推到式完成上面的需求
newlist = [int(i)*2 for i in varstr]
# print(newlist)  # [2, 4, 6, 8]


# 使用列表推到式+位运算完成
newlist = [int(i) << 1 for i in varstr]
# print(newlist)  # [2, 4, 6, 8]


# 二，带有判断条件的列表推到式
# 变量 = [变量或变量的处理结果 for i in 容器类型数据 条件表达式]
# 0-9 求所有的偶数，==> [0, 2, 4, 6, 8]
# 常规方法完成
newlist = []
for i in range(10):
    if i % 2 == 0:
        newlist.append(i)
# print(newlist) # [0, 2, 4, 6, 8]

# 列表推到式完成
newlist = [i for i in range(10) if i % 2 == 0]
# print(newlist)  # [0, 2, 4, 6, 8]


# 三， 带有条件判断的多循环的推到式
# [1,2,3],[3,1,4] ==> 把两个列表中的元素 两两组合，要求组合的元素不能重复
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 常规方法实现
newlist = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            newlist.append((x,y))
print(newlist)


# 使用列表推到式完成
newlist = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(newlist)



# 四，对于嵌套循环的列表推到式

'''
# 下面这个 3x4的矩阵，它由3个长度为4的列表组成，交换其行和列
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
]

==>
[
    [1, 5, 9], 
    [2, 6, 10], 
    [3, 7, 11], 
    [4, 8, 12]
]
'''
arr = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
]

# 常规方法完成
# newlist = []
# for i in range(4):
#     res = []
#     for row in arr:
#         res.append(row[i])
#     newlist.append(res)
# print(newlist)

# 使用列表推到式完成
newlist = [[row[i] for row in arr] for i in range(4)]
print(newlist)


# 练习作业，使用列表推到式完成九九乘法表