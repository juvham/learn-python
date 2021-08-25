#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 变量的定义方式

# 定义变量时 要注意遵守变量命名规范

# 第一种 变量定义方式
# a = 10
# b = 20

# 第二种定义方式
# a,b = 30,40


# 交换变量的数据
a = 10
b = 20

'''
利用python定义比变量的语法来实现 变量的数据交换
'''
a,b = b,a


'''
普通方式，完成变量数据的交换
1，把a变量的值 赋值给c  ，此时 c变量中 就是 10
2，把b变量的值 赋值给a  ， 此时 a变量中 就是 20
3，把c变量的值 赋值给b  ， 此时 b变量中 就是 10
'''
# c = a
# a = b
# b = c


print(a,b)

