#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 关键字参数收集

# kw ==> keyword

def love(a,b,c=3,*args,name,age,**kwargs):
    print(a,b,c)
    print(args) # 普通收集参数，会把多余的参数收集成为 元组
    print(name,age)
    print(kwargs) # 关键字参数收集，会把多余的关键字参数收集为 字典

# love(1,2,3,112,123,name='aaa',age=222,sex='ccc',aa='aa',bb='bb')
# love(a=111,b=222,c=333,123,name='a',age=20,sex=0) # X

# 注意行参声明的位置
# 普通参数，默认参数，收集参数，关键字参数，关键字收集参数
'''
极少情况下会出现上面五种行参
一般情况下： 普通参数，收集参数，关键字收集参数
'''



