#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 认识函数

# 不能在函数定义前调用函数
# love()  #NameError: name 'love' is not defined

# 函数的定义格式
def love():
    print('i')
    print('love')
    print('you')

# 函数的调用
love()
love()


# 函数的特征和注意
'''
1。函数定义后，不调用不执行
2。不能在函数定义前调用函数
3。函数的调用不受次数影响
4。函数的命名要遵守命名规范
    字母数字下划线，不能以数字开头
    严格区分大小写，不能使用关键字
    命名最好有意义，且不要使用中文
5。函数名不要冲突，冲突后会被覆盖
'''