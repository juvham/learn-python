#!/usr/bin/python
# -*- coding: utf-8 -*-

# 斐波那契数列
'''
0，1，1，2，3，5，8，13。。。
第0项如果是 0，那么第一项是 1，第二项也为 1，之后的第三项开始，每一项都是前面两个数的和
'''

# 获取用户输入的数据
num = int(input('你需要计算几项？'))

n1 = 0
n2 = 1
count = 2
# 从之后的数字开始计算
if num <= 0:
    print('请输入一个正整数。')
elif num == 1:
    print(f'斐波那契数列：{n1}')
else:
    print(f'斐波那契数列：{n1},{n2}',end=",")
    while count < num:
        # 计算当前数
        n3 = n1+n2
        print(n3,end=",")
        # 更新第一位和第二位数
        n1,n2 = n2,n3
        count += 1
'''
用户输入了 5
第一次运算 ： 0+1 = 1，n1 = 1，n2 = 1
第二次运算：  1+1 = 2，n1 = 1，n2 = 2
第三次运算：  1+2 = 3，n1 = 2，n2 = 3

'''

