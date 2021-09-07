#!/usr/bin/python
# -*- coding: utf-8 -*-
# 深拷贝与浅拷贝


# 浅拷贝 只能拷贝当前列表，不能拷贝列表中的多维列表元素

import copy
varlist = [1, 2, 3]
# 简单的拷贝 就可以把列表复制一份
newlist = copy.copy(varlist)
# 对新拷贝的列表进行操作，也是独立的
del newlist[1]
print(varlist,id(varlist))
print(newlist,id(newlist))
'''
[1, 2, 3] 4332224992
[1, 3] 4332227552
'''

# 多维列表
varlist = [1, 2, 3, ['a', 'b', 'c']]

# 使用copy函数 拷贝一个多维列表
newlist = copy.copy(varlist)

'''
print(newlist,id(newlist))
print(varlist,id(varlist))
[1, 2, 3, ['a', 'b', 'c']] 4361085408
[1, 2, 3, ['a', 'b', 'c']] 4361898496
'''
# 如果是一个被拷贝的列表，对它的多维列表元素进行操作时，会导致原列表中的多维列表也发生了变化
del newlist[3][1]

print(varlist,id(varlist))
print(newlist,id(newlist))

'''
通过id检测，发现列表中的多维列表是同一个元素（对象）
print(newlist[3],id(newlist[3]))
print(varlist[3],id(varlist[3]))
['a', 'c'] 4325397360
['a', 'c'] 4325397360
'''

# 深拷贝 就是不光拷贝了当前的列表，同时把列表中的多维元素也拷贝了一份

varlist = [1, 2, 3, ['a', 'b', 'c']]

# 使用 copy模块中 深拷贝方法 deepcopy
newlist = copy.deepcopy(varlist)
del newlist[3][1]

print(varlist)
print(newlist)

'''
    print(newlist[3],id(newlist[3]))
    print(varlist[3],id(varlist[3]))
    ['a', 'c'] 4483351248
    ['a', 'b', 'c'] 4483003568
'''
