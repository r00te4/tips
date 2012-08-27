#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_mmap.py
#     Desc:		Show mmap() function 
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-16 15:32:22
#     History:		
#=============================================================================
'''
# 在某些特殊行业，经常要面对十几GB乃至几十GB容量的巨型文件，而一个32位进程所拥有的虚拟地址空间只有232 = 4GB，显然不能一次将文件映像全部映射进来
# 对于这种情况只能依次将大文件的各个部分映射到进程中的一个较小的地址空间。这需要对上面的一般流程进行适当的更改： 
# 1）映射文件开头的映像。 
# 2）对该映像进行访问。 
# 3）取消此映像 
# 4）映射一个从文件中的一个更深的位移开始的新映像。 
# 5）重复步骤2，直到访问完全部的文件数据。

import mmap
import os

filename = "samples/sample.txt"

file = open(filename, "r+")
size = os.path.getsize(filename)

data = mmap.mmap(file.fileno(), size)

# basics
print data
print len(data), size

# use slicing to read from the file
# 使用切片操作读取文件
print repr(data[:10]), repr(data[:10])

# or use the standard file interface
# 或使用标准的文件接口
print repr(data.read(10)), repr(data.read(10))

# 这个文件必须以既可读又可写的模式打开( `r+` , `w+` , 或 `a+` ), 否则 mmap 调用会失败. 
