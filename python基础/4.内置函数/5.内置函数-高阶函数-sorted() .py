#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# ### sorted()
'''
sorted()
运行原理：
    把可迭代数据里面的元素，一个一个的取出来，放到key这个函数中进行处理，
    并按照函数中return的结果进行排序，返回一个新的列表
功能： 排序
参数：
    iterable 可迭代的数据 （容器类型数据，range数据序列，迭代器）
    reverse  可选，是否反转，默认为False，不反转， True反转
    key      可选， 函数，可以是自定义函数，也可以是内置函数
返回值： 排序后的结果
'''

arr = [3,7,1,-9,20,10]
# 默认按照从小到大的方式进行排序
# res = sorted(arr)  # [-9, 1, 3, 7, 10, 20]

# 可以按照从大到小的方式进行排序
# res = sorted(arr,reverse=True)  # [20, 10, 7, 3, 1, -9]

# 使用abs这个函数(求绝对值）作为sorted的key关键字参数使用
res = sorted(arr,key=abs)
# print(res)
'''
[ 3, 7, 1, -9, 20, 10]
  3  7  1  9   20  10
==>
  1  3  7  9  10  20
==>
  1  3  7  -9  10  20
'''

# 使用自定义函数
# def func(num):
#     print(num,num % 2)
#     return num % 2
#
# arr = [3,2,4,6,5,7,9]
#
# # 在sorted函数中使用自定义函数对数据进行处理
# res = sorted(arr,key=func)
# print(res)

## 优化版
arr = [3,2,4,6,5,7,9]
res = sorted(arr,key=lambda x:x%2)
print(res)




'''
3,2,4,6,5,7,9
==>
1 0 0 0 1 1 1
==>
2 4 6 3 5 7 9

'''





# ### map()

# ### reduce()

# ### filter()