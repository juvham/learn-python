#!/usr/bin/python
# -*- coding: utf-8 -*-

# 英文字符与字符检测相关函数

varstr = 'iloveyou'
# 一  大小写转换函数
# str.capitalize() 返回原字符串的副本，其首个字符大写，其余为小写。
res = varstr.capitalize()
print(res)
# str.title() 返回原字符的副本，把字符串中的每个单词首字母大写
res = varstr.title()
print(res)
# str.upper()  # 把字符串中的英文字符全部转为 大写
res = varstr.upper()
print(res)
# str.lower() # 把字符串中的英文字符全部转为 小写
res = res.lower()
print(res)
# 返回原字符串的副本，其中大写字符转换为小写，反之亦然。
res = varstr.swapcase()
print(res)

# 二，字符检测方法
# 检测当前的字符串中的英文字符否全部由 大写 字符组成
res = varstr.isupper()
print(res)
# 检测当前的字符串中的英文字符否全部由 小写 字符组成
res = varstr.islower()
print(res)
# 检测当前的字符串中的英文单词部分 是否符合 title 标题的 要求
res = varstr.istitle()
print(res)
# str.isalnum() #检测当前的字符串是否由字符(中文，英文字符，数字)组成
res = varstr.isalnum()
print(res)
# str.isalpha() # 检测当前的字符串是否由中英文字符组成（不包含数字和其它字符）
res = varstr.isalpha()
print(res)
# str.isdigit() # 检测当前的字符串是否由数字字符组成
res = varstr.isdigit()
print(res)
# str.isspace() # 检测当前的字符串是否由空格字符组成
res = varstr.isspace()
print(res)

# 检测一个字符串是否由指定的字符开头的，也可以指定开始和结束的位置
res = varstr.startswith('l')
print(res)
res = varstr.startswith('l', 1)
print(res)

# 检测一个字符串是否由指定的字符结尾的，也可以指定开始和结束的位置
res = varstr.endswith('love')
print(res)
res = varstr.endswith('love', 0, 5)
print(res)
