#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_skill.py
#     Desc:		glob module function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-27 15:57:34
#     History:		
#=============================================================================
'''

#glob模块是最简单的模块之一，内容非常少
    #用它可以查找符合特定规则的文件路径名, 跟使用 windows下的文件搜索差不多
    #查找文件只用到三个匹配符："*", "?", "[]"
        #"*"匹配0个或多个字符；
        #"?"匹配单个字符；
        #"[]"匹配指定范围内的字符，如：[0-9]匹配数字
#glob.glob
    #返回所有匹配的文件路径列表
    #它只有一个参数pathname，定义了文件路径匹配规则，这里可以是绝对路径，也可以是相对路径

import os
import re
import glob

#绝对路径
print glob.glob("/root/Desktop/Python/example/*/*.py")

#相对路径  
print glob.glob(r'../../*Oreilly*.chm') #相对路径  


#glob 事实上使用了 fnmatch 模块来完成模式匹配. 
#fnmatch 模块使用模式来匹配文件名
#fnmatch.fnmatch(file, "*.jpg")
#fnmatch.translate("*.py") 配合 re.match()
import fnmatch
for item in os.listdir("."):
    if fnmatch.fnmatch(item, "*.py"):
        print item

#pattern = fnmatch.translate("*.txt")
#for item in os.listdir("."):
    #if re.match(pattern, item):
#        print item
