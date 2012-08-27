#! /usr/bin/python
#!coding=utf8
'''
#=============================================================================
#     FileName:		tuple_fun.py
#     Desc:		This program will show tuple function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-25 18:02:03
#     History:		
#=============================================================================
'''
tuple_array = ("redflag", "qomo", "suse", "fedora")

# 取元组长度
print len(tuple_array)

# 取元组元素
print tuple_array
print tuple_array[1]
print tuple_array[::-1]

for item in tuple_array:
    print item

# 取元组脚标
print tuple_array.index("qomo")

# 元组和字符串一样是 不可变的 即你不能修改元组
# 有了列表,为什么还要用元组?
# 元组的不可变性可以提供某些整体性,你能肯定在一个程序中一个元组不会被另一个引用改变。一个来
# 自实践的原则:列表可以用于想变动的有序集合,元组则处理其它事情。

