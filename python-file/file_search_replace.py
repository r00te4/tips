#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_search.py
#     Desc:		This program will show how to search or replace a string from files
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-03 17:23:08
#     History:		
#=============================================================================
'''
import sys
import re

# 对文件的操作，无非： 读，写，查找，替换，合并，添加，分隔等
# 因为对文件我们可以整个读取，也可一行一行读取，所以可以使用之前处理字符串的任何一种方法来处理，如：
# 查找： re.match(), re. search(), re.findall()
# 替换： re.sub(), re.subn(), S.replace()
# 其它： re.split(), S.split(), S.splitlines(), S.strip(), string.Template, string.maketrans ......

if len(sys.argv) < 3:
    print "Usage: %s filename keywords" %sys.argv[0]
    sys.exit(1)

oldfile = open(sys.argv[1], "r")

#查找re.search
for line in oldfile.readlines():
    if re.search(sys.argv[2], line, re.I):
        print line

# 替换 re.sub
oldfile.seek(0)
for line in oldfile.readlines():
    line = line.rstrip('\n')
    #print re.sub(sys.argv[2], "Novell", line)
    print line.replace(sys.argv[2], "Novell") 


# 从文件中读取指定的某一行数据, linecache.getline, 
import linecache

the_line = linecache.getline(sys.argv[1], 3)
print the_line 


# 计算文件的行数
# 对于尺寸不大的文件，最简单的方法是将文件读取放入一个行列表中，然后计算列表的长度即可
count = len(open(sys.argv[1], 'rU').readlines())
print count

# 对于非常大的文件，用循环来计数是一个可行的方法, enumerate 返回两个参数：行数， 行内容
# enumerate 返回索引位置和对应的值, 从0开始计算， 可用于元组，列表 ...
for count, line in enumerate(open(sys.argv[1], 'rU')):
    count = count + 1 
    print count, line

# 当然也可以调用外部程序的统计功能，如 "wc -l", 使用os.popen() 调用
