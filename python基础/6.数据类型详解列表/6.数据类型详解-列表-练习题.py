#!/usr/bin/python
# -*- coding: utf-8 -*-

# 。练习题

# 1。 使用列表推到式完成 把字典中的键值对转换成 key=value 的数据格式
'''
字典 {'user':'admin','age':20,'phone':'133'}
列表 ['user=admin','age=20','phone=133']
'''
vardict =  {'user':'admin','age':20,'phone':'133'}
varlist = [i+'='+str(vardict[i]) for i in vardict]
print(varlist) # ['user=admin', 'age=20', 'phone=133']
# res = '&'.join(varlist) # user=admin&age=20&phone=133


# 2。 用列表推到式完成 把列表中的所有字符全部转为小写
# ['AAAAA','bbBb','CCCcc'] ==> ['aaaaa','bbbbb','ccccc']
varlist = ['AAAAA','bbBb','CCCcc']
newlist = [i.lower() for i in varlist]
print(newlist) # ['aaaaa', 'bbbb', 'ccccc']


# 3。 x 是0-5之间偶数，y是0-5之间奇数，把x，y组成一个元组，放到列表中
newlist = []
for x in range(6):
    for y in range(6):
        if x % 2 == 0 and y % 2 == 1:
            newlist.append((x,y))
print(newlist)

# 使用列表推到式完成
newlist = [(x,y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 == 1]
print(newlist)


# 4。 使用列表推到式 完成 九九乘法表

# 正序
# newlist = []
# for i in range(1,10):
#     for j in range(1,i+1):
#         res = f'{i}*{j}={i*j}'
#         newlist.append(res)

# python 中 可以一行代码 完成九九乘法表
# newlist = [f'{i}*{j}={i*j}' for i in range(1,10) for j in range(1,i+1)]
# print(newlist)

# 5。 求M，N中矩阵和元素的乘积
'''
M=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

N = [
    [2,2,2],
    [3,3,3],
    [4,4,4]
]
实现乘积的结果
（1）==> [2，4，6，12，15，18，28，32，36]
（2）==> [[2，4，6],[12，15，18],[28，32，36]]
'''

M=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

N = [
    [2,2,2],
    [3,3,3],
    [4,4,4]
]

newList = [M[x][y]* N[x][y] for x in range(3) for y in range(3)]
print(newList)
newList =   [[M[x][y]* N[x][y] for y in range(3)]  for x in range(3)]
print(newList)
