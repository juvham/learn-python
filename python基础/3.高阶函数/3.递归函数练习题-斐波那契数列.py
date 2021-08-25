#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 递归函数的练习

# 斐波那契数列 1，1，2，3，5，8，13。。。
# 求第n位上的数是多少？ 例如第六位 第6位 8

def feibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        print(n-1,n-2)
        return feibo(n-1) + feibo(n-2)

res = feibo(6)
print(res)
'''
5 4
4 3
3 2
2 1
2 1
3 2
2 1

feibo(6) ==>  feibo(5)                +          feibo(4)
                5                                 3
              ==> feibo(4) + feibo(3)             ==> feibo(3) + feibo(2)
                      3          2                     2         1
                            ==> feibo(2) + feibo(1)
                                   1         1
                 ==> feibo(3) + feibo(2)             ==> feibo(2) + feibo(1)
                       2          1                        1        1
                   ==> feibo(2) + feibo(1)
                            1      1

'''





# 实现一个数的阶乘：1*2*3*4*5*6*7