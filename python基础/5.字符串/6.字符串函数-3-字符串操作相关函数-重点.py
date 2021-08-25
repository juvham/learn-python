#!/usr/bin/python
# -*- coding: utf-8 -*-

# 字符串操作相关函数

vars = 'user_admin_id_123'

# str.split() 按照指定的字符进行分隔，把一个字符串分隔成一个列表
res = vars.split('_')  # ['user', 'admin', 'id', '123']
print(res)
# vars = 'uid=123&type=ab&kw=hh'
res = vars.split('&')
print(res)
for i in res:
    r = i.split('=')
    print(r.pop())

# 可以指定分隔的次数
res = vars.split('_', 2)  # ['user', 'admin', 'id_123']
print(res)
# str.rsplit()
res = vars.rsplit('_')  # ['user', 'admin', 'id', '123']
print(res)
res = vars.rsplit('_', 2)  # ['user_admin', 'id', '123']
print(res)

arr = ['user', 'admin', 'id', '123']
# str.join() 按照指定的字符，把容器类型中的数据链接成一个字符串
res = '@'.join(arr)  # user@admin@id@123
print(res)
vars = '###这是一个是#文章的标题##'
# 可以去除字符串左右两侧的指定字符
# str.strip()
res = vars.strip('#')
print(vars, len(vars))
print(res, len(res))

# str.lstrip() 去除字符串左侧的指定字符
# str.rstrip() 去除字符串右侧的指定字符


# str.replace() 替换
vars = 'iloveyoutosimidailoveyou'
# res = vars.replace('love','like')
res = vars.replace('love', 'LOVE', 1)
print(res)


# 了解
vars = 'love'
res = vars.center(10)
print(res)
res = vars.center(12, '*')
print(res)
res = vars.ljust(10, '*')
print(res)
res = vars.rjust(10, '*')
print(res)
