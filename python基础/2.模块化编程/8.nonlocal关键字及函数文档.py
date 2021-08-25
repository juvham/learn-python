#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# nonlocal

# 变量和函数都有作用域
# 在内函数中如何使用上一层函数中的局部变量？

'''
在内函数中如果想使用外层函数的变量，
那么需要使用 nonlocal 关键字 引用,
可以引用上一层函数中定义的局部变量，
但依然不能提升为全局变量

'''


# 定义一个外层函数
def outer():
    '''
    这里是让你些当前函数的文档说明的。
    需要说明当前函数的作用，
    如果当前函数还有行参，那么也需要对行参进行一一说明
    name： 这个是一个name参数，有什么作用。。。
    age ： 这个表示当前的一个年龄
    :return:  此处说明当前函数的返回值。。。
    '''
    # 外函数的局部变量
    num = 10
    # 内函数，局部函数，在函数的内部定义的函数

    def inner():
        # nonlocal 关键字在局部函数中使用，
        nonlocal num  
        # 可以引用上一层函数中定义的局部变量，
        # 但依然不能提升为全局变量
        num += 1
        print(num)
    inner()


outer()

# print(num)


# 关于函数的文档
print(globals())

print(__name__)  # 获取当前脚本的文件名，
print(__doc__)  # 获取当前脚本的说明文档
# print(outer.__doc__) # 获取当前函数的说明文档
'''
魔术变量
__name__  ==> 当前脚本如果作为主程序，那么值是 __main__,
如果是当做一个模块，在另外一个脚本中引用去使用，那么值就是当前文件的名字
__doc__   ==> 当前脚本的文档说明 在当前脚本当中的第一个,
三引号注释就是当前脚本的说明文档


{
    '__name__': '__main__', 
    '__doc__': '\n在内函数中如果想使用外层函数的变', 
    '__package__': None,
     '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x110444350>, 
     '__spec__': None, 
     '__annotations__': {}, 
     '__builtins__': <module 'builtins' (built-in)>, 
     '__file__': '/Users/yc/Desktop/code/8.nonlocal关键字.py', 
     '__cached__': None, 'outer': <function outer at 0x1104938c0>
}

'''
