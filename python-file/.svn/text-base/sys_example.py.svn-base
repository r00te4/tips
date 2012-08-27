#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		sys_example.py
#     Desc:		show sys module function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-23 15:45:06
#     History:		
#=============================================================================
'''

import sys

#使用sys模块获得脚本的参数: sys.argv
if len(sys.argv)<2:
    print "Usage: %s arg1" %sys.argv[0]
    sys.exit()
 

# 使用sys模块获得当前平台: sys.platform
# 典型的平台有Windows 9X/NT(显示为 win32 ), 以及 Macintosh(显示为 mac ) 
# 对于 Unix 系统而言, platform 通常来自 "uname -r" 命令的输出, 例如 irix6 , linux2 , 或者 sunos5 (Solaris). 
print sys.platform

print sys.stdin.readline()

print sys.modules

print sys.path

#系统相关的信息模块 import sys
#sys.argv是一个list,包含所有的命令行参数.
#sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.
#sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a
#sys.exit(exit_code) 退出程序
#sys.modules 是一个dictionary，表示系统中所有可用的module
#sys.platform 得到运行的操作系统环境
#sys.path 是一个list,指明所有查找module，package的路径
