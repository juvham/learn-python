#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# 高阶函数-reduce()

'''
reduce(func,iterable)
功能：
    每一次从 iterable 拿出两个元素，放入到func函数中进行处理，得出一个计算结果，
    然后把这个计算结果和iterable中的第三个元素，放入到func函数中继续运算，
    得出的结果和之后的第四个元素，加入到func函数中进行处理，以此类推，直到最后的元素都参与了运算
参数：
    func： 内置函数或自定义函数
    iterable： 可迭代的数据
返回值：最终的运算处理结果
注意： 使用 reduce函数时，需要导入 from functools import reduce
'''

from functools import reduce

### (1) [5,2,1,1] ==> 5211

# 普通方法
# varlist = [5,2,1,1]
# res = ''
# for i in varlist:
#     res += str(i)
# res = int(res)
# print(res,type(res))
'''
5 2 1 1
5 * 10 + 2 == 52
52 * 10 + 1 == 521
521 * 10 + 1 == 5211
'''

# 使用 reduce完成
# def myfunc(x,y):
#     return x*10+y
# varlist = [5,2,1,1]
# # 调用函数
# res = reduce(myfunc,varlist)
# print(res,type(res))

# （2） 把字符串的 '456' ==> 456
#  要求不能使用int方法进行类型的转换时，如何解决上面的问题

# 定义函数，给定一个字符串的数字，返回一个整型的数字
def myfunc(s):
    vardict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return vardict[s]

# 1.先使用 map函数，把数字字符串，转为整型的数字
iter1 = map(myfunc,'456')

# 2. 把数字列表中的值，使用lambda进行二次处理
iter2 = reduce(lambda x,y:x*10+y,iter1)
print(iter2)







