#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_rw.py
#     Desc:		This program will show the the file read/wirte/seek/ functions
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-25 15:25:02
#     History:		
#=============================================================================
'''
import sys
import re

if len(sys.argv) < 3:
    print "Usage: %s filename newfile" %sys.argv[0]
    sys.exit()

# 创建一个文件对象：open(file, "rwab")
# 第一个参数是文件名称，包括路径；
# 第二个参数是打开的模式mode
    #'r'：只读（缺省, 如果文件不存在，则抛出错误）
    #'w'：只写（如果文件不存在，则自动创建文件）
    #'a'：附加到文件末尾
    #'r+'：读写
# 如果需要以二进制方式打开文件，需要在mode后面加上字符"b"，比如"rb""wb"等

oldfile = open(sys.argv[1], "r")
newfile = open(sys.argv[2], "w")

# 文件对象提供了三个“读”方法： .read()、.readline() 和 .readlines()
# 每种方法可以接受一个变量以限制每次读取的数据量，但它们通常不使用变量
# .read([size]) 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中，但对于连续的面向行的处理，它却是不必要的，并且如果文件大于可用内存，则不可能实现这种处理
# .readline([size]) 每次只读取一行，通常比 .readlines()慢得多, 仅当没有足够内存可以一次读取整个文件时，才应该使用.readline()
# .readlines([size]) 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理

for line in oldfile.readlines():
    line = re.sub('\w+@\w+.\w+', "030802127@163.com", line)
    line = re.sub('中国', "Forrest", line)
    newfile.write(line)

# 同样，文件对象提供了三个“写”方法： .write()、.writeline() 和 .writelines()


# 文件中的内容定位: .seek()
# 读取之后，文件指针到达文件的末尾，如果再来一次f.read()将会发现读取的是空内容，如果想再次读取全部内容，必须将定位指针移动到文件开始：f.seek(0)  
# f.seek(offset, from_what)  
# from_what表示开始读取的位置，
# offset表示从from_what再移动一定量的距离
# 比如f.seek(10, 3) 表示定位到第三个字符并再后移10个字符, from_what值为0时表示文件的开始，它也可以省略，缺省是0即文件开头


# 关闭文件释放资源 .close()
# 文件操作完毕，一定要记得关闭文件f.close()，可以释放资源供其他程序使用

# 除非读取的文件非常大，不然一次性读出所有内容放进内存并进一步处理，是最快最方便的办法；
# 在Unix或类Unix系统中，文本文件和二进制文件其实并没有什么区别， windows系统中， 换行符不是标准的'\n', 而是'\r\n';
# python会自动把换行符转化成'\n', 所以对于二进制文件，需要明确告诉python 'rb'参数，这样就不会做任何转化了;
# 如果不确定某文本文件会用什么样的换行符， 可以将open第二个参数设定为'rU',指定通用换行符转化.

# Python 对超大文件的处理:
# 1.多线程(Multiple Thread)的处理方式
# 2.多进程(Multiple Processes)的处理方式
# 3.存储器映像(Memory Mapping)的处理方式
