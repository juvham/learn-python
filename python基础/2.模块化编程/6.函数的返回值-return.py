#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 函数的返回值

'''
函数可以分为两类
    1。执行过程函数： 函数体内完成一定的功能既可，没有返回值
    2。具有返回值的函数： 函数体内完成一定的功能，并且返回一个结果到函数调用处
'''

'''
函数中可以使用 return 进行数据的返回
可以使用return 返回 任意内容或数据
return 会把返回值，返回到函数调用出
return 意味着函数的结束，return之后的代码不在执行
如果在函数中没有使用return  或者 return后面没有任何内容，那么默认返回 None
'''

# 在一个函数中，可以返回一些内容，也可以不返回

# 没有返回值的函数，或者理解为，没有指定返回内容，默认返回类 None
def love(a, b):
    print(f'{a} i love you {b}')

# r = love('奥特曼','小怪兽')
# print(r)

# None  是一个特殊的数据，表示什么都没有,空


# 如果需要在函数中指定返回内容，可以使用 return 关键字
def love(a,b):
    res = f'{a} i love you {b}'
    # 可以在函数体内，使用return 返回任意内容
    print(1)
    return res

# love('奥特曼','小怪兽')

# 调用带有返回值的函数时，函数中的返回值，会返回到函数调用处
# print(love('老鼠','猫咪'))
# r = love('狼','羊')
# print(r)


# 假设有这样一个需求，定义一个函数，完成两个数的计算，并把结果输出
# def jia(n1,n2):
#     res = n1+n2
#     print(res)
# jia(2,5)

# 需求改变，定义一个函数，完成两个数的计算，并把结果返回
def jia(n1,n2):
    res = n1+n2
    return res

r = jia(2,4)
print(r)