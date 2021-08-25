#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 变量的作用域

'''

局部变量
    函数内定义的变量，局部变量，在函数外不能使用

全局变量
    在函数内部使用 global 直接定义的变量，就是全局变量，函数内外都可以使用
    在函数外定义的变量，在函数内使用 global 关键字进行声明，那么也是全局变量

globals()  获取全局数据
locals()  获取当前作用域的数据

    在函数外定义的变量，函数可以访问，但是不能更改

数据类型的分类：
    可变数据类型：在函数外定义的变量，在函数可以使用，
        列表和字典
    不可变数据类型：在函数外定义的变量，在函数内只能访问，不能使用其它操作
'''

num = 10
varlist = [1,2,3]
vardict = {'a':'a','b':'b'}

def func():
    global num
    print(num) # 在函数内可以获取函数外部的变量
    num += 20 # 在函数内不能直接更改函数外的变量

    # print(varlist)
    # varlist[2] = 'aa'

    # print(vardict)
    # vardict['a'] = 'aa'

    # 函数内定义的变量 局部变量
    love = 20
    love += 1
    # print(love)

    # 在函数内部使用 global关键字定义的变量就是全局变量
    global live
    live = 'iliveyou'

    # 在函数内部使用 global和locals
    # print(globals())
    # print(locals())

func()
# print(num)
# print(love) # 函数内定义的变量，在函数外不能使用
# print(varlist)
# print(vardict)

# print(live)
# live = 'live'
# print(live)


# 在函数外使用函数
# globals() 获取全局变量数据
# locals()  获取当前作用域的变量数据
# print(globals())
# print(locals())
# 问：为什么上面两个函数的结果一模一样
# 因为当前区域就是全局区域


# 不光变量有作用域，函数一样也有相同的作用域

def outer():
    print('this is outer function...')
    # 在函数内定义的函数，称为 局部函数，函数外无法使用
    def inner():
        print('this is inner function...')
    inner()

outer()
# inner()