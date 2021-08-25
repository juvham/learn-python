#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 关于函数的参数

# 带有参数的函数，如何定义

# 在定义函数时，在小括号内可以定义行参（形式上的参数）
def love(w):
    print(f'i love you {w}')

# 调用带有行参的函数时，需要传递参数（实参）
# love('猩猩')

# love() # TypeError: love() missing 1 required positional argument: 'w'

# 带有多个参数的函数
def love(x,w):
    print(f'{x} i love you {w}')


# 函数定义了几个参数，那么在调用时就必须指定按顺序进行参数的传递
love('狗蛋','猫咪')
