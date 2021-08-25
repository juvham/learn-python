#!/usr/bin/python
# -*- coding: utf-8 -*-

# 流程控制-分支结构 - 十二生肖

# 注意： 在书写代码时，一定严格遵守python的语法要求

# if True:
#     pass # pass 在代码库中专门用与 占位
#     print(111) # 在编写python脚本时，相同代码块要保持相同的缩进

'''
十二生肖
让用户输入一个四位数的年份，来计算当前这个年份所对应的 生肖年，
申猴 酉鸡 戌狗 亥猪 子鼠 丑牛 寅虎 卯兔 辰龙 巳蛇 午马  未羊
0   1    2    3    4   5   6   7   8    9   10   11
2000 ==> 辰龙
2019 ==> 亥猪

获取用户输入 input()，print() 打印输出
'''
#
# # 获取用户输入的年份
# year = int(input('请输入四位数的年份：'))
# # print(year%12)
# if year % 12 == 0:
#     print(f'{year}年是 ==> 申猴')
# elif year % 12 == 1:
#     print(f'{year}年是 ==> 酉鸡')
# elif year % 12 == 2:
#     print(f'{year}年是 ==> 戌狗')
# elif year % 12 == 3:
#     print(f'{year}年是 ==> 亥猪')
# elif year % 12 == 4:
#     print(f'{year}年是 ==> 子鼠')
# elif year % 12 == 5:
#     print(f'{year}年是 ==> 丑牛')
# elif year % 12 == 6:
#     print(f'{year}年是 ==> 寅虎')
# elif year % 12 == 7:
#     print(f'{year}年是 ==> 卯兔')
# elif year % 12 == 8:
#     print(f'{year}年是 ==> 辰龙')
# elif year % 12 == 9:
#     print(f'{year}年是 ==> 巳蛇')
# elif year % 12 == 10:
#     print(f'{year}年是 ==> 午马')
# elif year % 12 == 11:
#     print(f'{year}年是 ==> 未羊')
# else:
#     print('计算错误，年份不对')

# 程序的优化

# 获取用户输入的年份
year = int(input('请输入四位数的年份：'))
# 定义十二生肖 列表
varlist = ['申猴' ,'酉鸡' ,'戌狗' ,'亥猪' ,'子鼠' ,'丑牛' ,'寅虎' ,'卯兔' ,'辰龙' ,'巳蛇' ,'午马'  '未羊']
print(varlist[year % 12])





