#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 百钱买百鸡
'''
一共有100块钱，需要买100只鸡
公鸡 == 3元 ==> 33只
母鸡 == 1元 ==> 100只
小鸡 == 0.5元 ==> 200只
问：100块钱买100只鸡，一共有多少种方案

1。都买母鸡
'''
# num = 1
# for gj in range(1,34):
#     for mj in range(1,101):
#         for xj in range(1,201):
#             # 判断是否为100只，是否花费100元
#             if gj+mj+xj == 100 and gj*3 + mj + xj*0.5 == 100:
#                 print(f'公鸡{gj}只,母鸡{mj}只,小鸡{xj}只,{gj*3 + mj + xj*0.5}')
#                 num += 1
# print(num)


# 优化版
count = 0
num = 1
for gj in range(1,34):
    for mj in range(1,101):
        xj = 100 - gj - mj
        count += 1
        # 判断是否为100只，是否花费100元
        if gj+mj+xj == 100 and gj*3 + mj + xj*0.5 == 100:
            print(f'公鸡{gj}只,母鸡{mj}只,小鸡{xj}只,{gj*3 + mj + xj*0.5}')
            num += 1
print(num)
print(count)


