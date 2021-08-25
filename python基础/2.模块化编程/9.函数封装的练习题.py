#!/usr/bin/python
# -*- coding: utf-8 -*-

# 函数封装的练习题

# 打印九九乘法表，矩形，十二生肖。。

# 定义函数，打印九九乘法表
def jiujiu(n=0):
    '''
    当前函数的功能就是 打印 九九乘法表
    n=0; 控制 正向输出 和 反向输出 九九乘法表 ，0为正向 默认，1为反向
    '''
    if n == 0:
        rs = range(1, 10)
    else:
        rs = range(9, 0, -1)
    for x in rs:
        for y in range(1, x+1):
            print(f'{x}x{y}={x*y}', end=" ")
        print()


jiujiu(1)


# 封装打印矩形的函数 juxing(x=10,y=10)
def juxing(n,x,y):
    print('#'*x)
    for i in range(1,y+1):
        if n == 1:
            print('#'*x)
        elif n == 0:
            nbsp = ' ' * (x-1)
            print(f'#{nbsp}# ')
    print('#'*x)

juxing(n=0,x=20,y=20)
