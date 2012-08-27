#! /usr/bin/python
#!coding=utf8
'''
#=============================================================================
#     FileName:		skill.py
#     Desc:		This program will show all the skills about python, such as lambda, zip, filter, yield
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-26 15:28:53
#     History:		
#=============================================================================
'''

# lambda其实就是一条语句，lambda(x):body
# x是lambda函数的参数，参数可以有任意多个(包括可选参数);
# body是函数体，只能是一个表达式，并且直接返回该表达式的值
fun = lambda x,y: x+y
print fun(100,200)


# filter函数的功能相当于过滤器
# 调用一个布尔函数bool_func来迭代遍历每个seq中的元素；
# 返回一个使bool_seq返回值为true的元素的序列

list = ["about", "hello", "hongsun", "boy", "house"]
def func(str):
    return str.startswith("h")

print filter(func, list)


# map 函数是filter的伴侣，map 接受一个函数和一个列表作为参数，并以列表中每个元素顺序地调用函数返回一个新的列表
list = [1,3,5]
def func(num):
    return num*2

print map(func, list)


# reduce内建函数是一个二元操作函数，用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给reduce中的函数 func()（必须是一个二元操作函数）
# 先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果
array = (1,2,3,4,5,6,7,8,9)
def add(x,y):
    return x+y
print reduce(add, array)                # 1+2+3+4+5+6+7+8+9

print reduce(lambda x,y: x+y, array)    # 用lambda要简单得多



# zip函数接受任意多个序列作为参数，将所有序列按相同的索引组合成一个元素, 使各个序列合并成的tuple的新序列
# 新的序列的长度, 以最短的序列为准
# 另外(*)操作符与zip函数配合可以实现与zip相反的功能，即将合并的序列拆成多个tuple
# itertools 的izip也可实现同样功能

list1 = ["a", "b", "c"]
list2 = ["1", "2", "3", "4"]
print zip(list1, list2)

print dict(zip(list1, list2))

print zip(*zip(list1, list2))



# range/range的区别: 
# 用range等于先malloc足够的内存，然后完成值的准备，等待调用(遍历等等)
# 而xrange则不这么干，什么时候要的时候，什么时候给值
# 在Python 2.x中，type(range(10))是一个List，是内存中的静态数据；而type(xrange(10))则是一个range type。
# 在Python 3.x，xrange彻底替代了range函数。
print type(range(10))
print type(xrange(10))


# yield ，可以让你的函数中断， 当再次回来这个函数时从这个中断处继续执行, 每次发生next()调用，函数执行完yield语句之后在挂起，这时返回yield的值
# yield 可以解读为"返回然后等待",
# 如果所有yield语句完成，这时再次调用next()，则发生StopIteration异常
def gen():
    print "one"
    yield 1
    print "two"
    yield 2
    print "three"
    yield 3

print type(gen)
print type(gen())

# generator的方法之一就是next()。
a=gen()
a.next()
a.next()
a.next()
#a.next() 三次yield调用完后，如果再次调用，则异常


# Python 数据概念:
# 列表 (list)
# 元组 (tuple)
# 字典 (dict)
# 集合 (set)
# 模块 (module)
# 类 (class)
