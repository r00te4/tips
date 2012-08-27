#! /usr/bin/python
'''
#=============================================================================
#     FileName:		mul_args.py
#     Desc:		This program will show the *args and **kwargs function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-25 15:15:32
#     History:		
#=============================================================================
'''

def show_args(*args):
    print "This will show *args function:"
    for arg in args:
        print arg

show_args(1,2,3,4)
show_args("hello", "world")

def show_kwargs(**args):
    print "This will show **args function:"
    for key, value in args.items():
        print "key is: %s, value is: %s" %(key, value)

show_kwargs(foo="bar", spam="eggs")


#python提供了两种特别的方法来定义函数的参数，允许函数接受过量的参数，不用显式声明参数

#1. 位置参数 *args
#在参数名之前使用一个星号，就是让函数接受任意多的位置参数
#python把参数收集到一个元组中，作为变量args
#显式声明的参数之外如果没有位置参数，这个参数就作为一个空元组

#2. 关键字参数 **kwargs
#python在参数名之前使用2个星号来支持任意多的关键字参数
#kwargs是一个正常的python字典类型，包含参数名和值
#如果没有更多的关键字参数，kwargs就是一个空字典
