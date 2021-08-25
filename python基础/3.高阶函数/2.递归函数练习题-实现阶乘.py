#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 实现阶乘 求一个数的阶乘结果  7 1*2*3*4*5*6*7

def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n*jiecheng(n-1)

res = jiecheng(7)
print(res)

'''
jiecheng(7) = 5040
7*jiecheng(6)
    6*jiecheng(5)
        5*jiecheng(4)    
            4*jiecheng(3)    
                3*jiecheng(2)    
                    2*jiecheng(1) 
                        jiecheng(1) ==> 1   
                    2*1 ==> 2
                3*2  ==> 6
            4*6 ==> 24
        5*24 ==> 120
    6*120 ==> 720
7*720 ==> 5040
'''

'''
递归函数的效率并不高，尽量能不用就不用。。。
一个函数如果调用后，没有结束，那么在栈空间中就一直存在，直到这个函数运算结束才销毁
'''




