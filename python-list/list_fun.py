#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		list_fun.py
#     Desc:		This program will show list function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-25 17:29:51
#     History:		
#=============================================================================
'''

office_list = ["computer", "mouse", "keyboard", "webcam"]

# 计算元素长度len
print len(office_list)

# 取元素
print office_list
print office_list[1]
print office_list[-1]
print office_list[::-1]

for item in office_list:
    print item

# 添加元素 append()， 加至结尾
office_list.append("battery")
print office_list

# 追加列表 extend(), append追加的是一个值，extend追加的是一个数组(列表)
a = [1,2,3,4]
b = ("a","b","c")
a.extend(b)
print a

# 插入元素 insert(), 指定脚标
office_list.insert(2, "touchpad")
print office_list

# 返回元素脚标 index()
print office_list.index("webcam")

# 返回元素在列表中出现的次数 count()
print office_list.count("computer")

# 删除元素 remove()
office_list.remove("mouse")
print office_list

# 删除指定脚标的元素，并返回此元素, pop(i), 若pop()，则删除最后一个元素，并返回
print "Will remove first option:", office_list.pop(1)

# 排序元素 sort()
office_list.sort()
print office_list

# 反转元素 reverse()
office_list.reverse()
print office_list
