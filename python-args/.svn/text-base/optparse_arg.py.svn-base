#! /usb/bin/python
#coding=utf8
#=============================================================================
#     FileName:		optparse_arg.py
#     Desc:		This program will show optparse function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-06 16:46:29
#     History:		
#=============================================================================

from optparse import OptionParser

usage = "usage: %prog [options] arg1 arg2"
version = "0.1.1"
parser = OptionParser(usage=usage, version=version)

#parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=True, help="make lots of noise")
parser.add_option("-f", "--file",  dest="filename", help="input a file name")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="make lots of noise")
parser.add_option("-l", "--list", action="store_false", dest="list", help="list all the commands")

(options, args)=parser.parse_args()

if options.verbose:
    print "this is verbose, true"
else:
    print "this is verbose, false"

if options.filename:
    print "this is filename, ture"
else:
    print "this is filename, false"

if options.list:
    print "this is list, ture"
else:
    print "this is list, false"

print options
print args


#上面的例子可以看出OptionParser的基本用法：
#1. 实例化OptionParser：    parser = OptionParser()
#2. 添加选项：            parser.add_option(opt_str, ..., attr=value, ...)
#3. 然后是调用parse_args来解析命令行参数：(options, args) = parser.parse_args()

#action:
    #默认store, 即选项后面要有选项值, 如 -f file,  options.filename 即'filename': 'file'   真
    #选项store_true, 即选项后面不需要带选项值, 如 -v, options.verbose 即'verbose': 'Ture' 真
    #选项store_false, 即选项后面不管有没有选项值，始终为false

#type：选项值类型，默认为string。支持int，float，long和complex

#dest：选项值保存在选项对象中管理的属性名, 最终由  options.属性名  来引用判断

#default属性已经过时，建议使用parser.set_defaults()来更显式的设置默认值，如上例可以改为parser.set_defaults(verbose=True)

#判断用户启用了哪些参数, 只需要判断options的各个属性是否为非空就行了.
