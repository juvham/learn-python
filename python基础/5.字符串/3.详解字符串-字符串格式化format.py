#!/usr/bin/python
# -*- coding: utf-8 -*-

# format() 格式化字符串  f

# 1 format  普通方式
a = '李白'
vars = '{}乘舟将欲行，忽闻岸上踏歌声'.format(a)
print(vars)
vars = '{}乘舟将欲行，忽闻岸上{}'.format(a, '踏歌声')
print(vars)
# 2 format  通过索引传参                   0   1   2
vars = '{2}乘舟将欲行，忽闻岸上{1}'.format('a', 'b', 'c')
print(vars)

# 3 format  关键字传参
vars = '{a}乘舟将欲行，互闻岸上{b}'.format(a='李白', b='踏歌声')
print(vars)

# 4 format  容器类型数据传参
vars = '豪放派：{0[0]}，婉约派：{0[1]}，蛋黄派：{0[2]}'.format(['李白', '辛弃疾', '达利园'])
print(vars)
data = {'a': '辛弃疾', 'b': '蛋黄派'}
vars = '{a}乘舟将欲行，互闻岸上{b}'.format(**data)
print(vars)
# 3.7中新增的 格式化方法 f方法
vars = f'{data["a"]}乘舟将欲行，互闻岸上{data["b"]}'
print(vars)

# 限定小数的位数
vars = '圆周率是多少：{:.2f}'.format(3.1415926)
print(vars)
