#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 矩形打印

# 输出十行十列 ★ ☆
# print('☆')

# 第一种
# num = 1
# while num <= 100:
#     print('☆',end=" ")
#     # 判断是否需要换行
#     if num % 10 == 0:
#         print()
#     num += 1

# 第二种
# num = 0
# while num < 100:
#     print('☆',end=" ")
#     # 判断是否需要换行
#     if num % 10 == 9:
#         print()
#     num += 1


# 隔列换色
# num = 0
# while num < 100:
#     # 判断当前数是奇数还是偶数
#     if num % 2 == 0:
#         print('★',end=" ")
#     else:
#         print('☆',end=" ")
#
#     # 判断是否需要换行
#     if num % 10 == 9:
#         print()
#     num += 1

'''
☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★  
☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★  
☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★  
'''




# 隔行换色
'''
☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ 
☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ 
☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
'''

num = 0
while num < 100:
    # 以当前的行数作为基数，对2取余，判断奇偶行
    if num // 10 % 2 == 0:
        print('☆',end=" ")
    else:
        print('★',end=" ")

    # 判断是否需要换行
    if num % 10 == 9:
        print()
    num += 1

# 三角形  菱形