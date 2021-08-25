#!/usr/bin/python
# -*- coding: utf-8 -*-
# # 转义字符

# \ 续行符

# 续行符
vars = '123' \
       '456'
print(vars)

# \ 转义符，在字符出现的特定字符有着特定的意义
# \n  代表一个换行符
vars = '岁月是把杀猪刀，\n\n但是它拿长得丑的人一点办法都没有。。。'
print(vars)
# \r 代表光标的位置（从\r出现的位置开始作为光标的起点）
vars = '岁月是把杀猪刀，\r但是它拿长得丑的人一点办法都没有。。。'
print(vars)
# \t 水平制表符（table 缩进）
vars = '岁月是把杀猪刀，\t但是它拿长得丑的人一点办法都没有。。。'
print(vars)
# \b 退格符
vars = '岁月是把杀猪刀，\b但是它拿长得丑的人一点办法都没有。。。'
print(vars)
# \\ 一个\是转义符，在这个符号前在定义一个\ 就会取消转义。变成一个普通的\输出
vars = '岁月是把杀猪刀，\\n但是它拿长得丑的人一点办法都没有。。。'
print(vars)
# 把转义字符作为普通字符输出,在字符串的前面加 r''
vars = r'岁月是把杀猪刀，\b但是它拿长得丑的人一点办法都没有。。。'
print(vars)
